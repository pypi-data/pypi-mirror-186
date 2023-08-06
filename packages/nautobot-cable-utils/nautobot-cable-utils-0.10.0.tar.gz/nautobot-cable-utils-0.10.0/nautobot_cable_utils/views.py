from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.contenttypes.models import ContentType
from django.db import transaction
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import View, FormView

from nautobot.core.views import generic
from nautobot.dcim.choices import CableStatusChoices
from nautobot.dcim.models import Cable, Device, Interface, FrontPort
from nautobot.core.views.generic import (
    BulkDeleteView, BulkImportView, GetReturnURLMixin, ObjectEditView,
    ObjectListView
)
from nautobot.utilities.forms import ConfirmationForm
from nautobot.extras.models.statuses import Status

from . import filters, forms, tables
from .cable_router import CablePath
from .forms import CableRouterVerifyForm, CableRouterLinkToInterfaceForm, \
    CableRouterLinkToFrontPortForm
from .models import CableTemplate, MeasurementLog
from .tables import NeededCableTable


class ReconnectView(PermissionRequiredMixin, GetReturnURLMixin, View):
    permission_required = 'dcim.add_cable'
    template_name = 'nautobot_cable_utils/cable_connect.html'

    def dispatch(self, request, *args, pk=None, **kwargs):
        self.obj = Cable.objects.get(pk=pk)

        idx = (self.obj.termination_a_type.model, self.obj.termination_b_type.model)
        idx_sorted = tuple(sorted(idx))
        if idx != idx_sorted:
            termination_a = self.obj.termination_a
            self.obj.termination_a = self.obj.termination_b
            self.obj.termination_b = termination_a

        self.form_class = {
            ('circuittermination', 'circuittermination'): forms.ConnectCircuitTerminationForm,
            ('circuittermination', 'rearport'): forms.ConnectCircuitTerminationToRearPortForm,
            ('consoleport', 'consoleserverport'): forms.ConnectConsolePortToConsoleServerPortForm,
            ('consoleport', 'frontport'): forms.ConnectConsolePortToFrontPortForm,
            ('consoleport', 'rearport'): forms.ConnectConsolePortToRearPortForm,
            ('consoleserverport', 'frontport'): forms.ConnectConsoleServerPortToFrontPortForm,
            ('consoleserverport', 'rearport'): forms.ConnectConsoleServerPortToRearPortForm,
            ('powerfeed', 'powerport'): forms.ConnectPowerfeedToPowerPortForm,
            ('poweroutlet', 'powerport'): forms.ConnectPowerOutletToPowerPortForm,
            ('circuittermination', 'interface'): forms.ConnectCircuitTerminationToInterfaceForm,
            ('frontport', 'interface'): forms.ConnectFrontPortToInterfaceForm,
            ('interface', 'rearport'): forms.ConnectInterfaceToRearPortForm,
            ('interface', 'interface'): forms.ConnectInterfaceForm,
            ('frontport', 'frontport'): forms.ConnectFrontPortForm,
            ('frontport', 'rearport'): forms.ConnectFrontPortToRearPortForm,
            ('circuittermination', 'frontport'): forms.ConnectCircuitTerminationToFrontPortForm,
            ('rearport', 'rearport'): forms.ConnectRearPortForm,
        }[idx_sorted]

        return super().dispatch(request, *args, **kwargs)

    def prefill_form(self, initial_data, termination):
        o = getattr(self.obj, termination)
        if o and hasattr(o, 'device'):
            device = o.device
            initial_data['{}_device'.format(termination)] = device
            if device.site:
                initial_data['{}_site'.format(termination)] = device.site
            if device.rack:
                initial_data['{}_rack'.format(termination)] = device.rack

    def get(self, request, *args, **kwargs):
        # Parse initial data manually to avoid setting field values as lists
        initial_data = {k: request.GET[k] for k in request.GET}

        self.prefill_form(initial_data, 'termination_a')
        self.prefill_form(initial_data, 'termination_b')

        form = self.form_class(instance=self.obj, initial=initial_data)

        return render(request, self.template_name, {
            'obj': self.obj,
            'obj_type': Cable._meta.verbose_name,
            'form': form,
            'return_url': self.get_return_url(request, self.obj),
        })

    def post(self, request, *args, **kwargs):
        assigned_cable_template = None

        with transaction.atomic():
            try:
                if hasattr(self.obj.termination_a, '_path') and self.obj.termination_a._path_id:
                    self.obj.termination_a._path = None
            except CablePath.DoesNotExist:
                pass
            try:
                if hasattr(self.obj.termination_b, '_path') and self.obj.termination_b._path_id:
                    self.obj.termination_b._path = None
            except CablePath.DoesNotExist:
                pass

            assigned_cable_template = CableTemplate.objects.filter(cable=self.obj).first()

            self.obj.delete()
            self.obj.pk = None
            self.obj._state.adding = True

            self.obj.termination_a.cable = None
            self.obj.termination_b.cable = None

            form = self.form_class(request.POST, request.FILES, instance=self.obj)
            if form.is_valid():
                obj = form.save()

                if assigned_cable_template is not None:
                    # restore cable template if previously assigned
                    assigned_cable_template.cable = obj
                    assigned_cable_template.save()

                redirect_url = self.get_return_url(request, obj)
                return redirect(redirect_url)

            return render(request, self.template_name, {
                'obj': self.obj,
                'obj_type': Cable._meta.verbose_name,
                'form': form,
                'return_url': self.get_return_url(request, self.obj),
            })


class CommissionView(PermissionRequiredMixin, GetReturnURLMixin, View):
    permission_required = 'dcim.edit_cable'
    template_name = 'nautobot_cable_utils/commission_cable.html'

    def get(self, request, pk=None):
        cable = get_object_or_404(Cable, pk=pk)
        form = forms.CommissionForm(initial={'cable': cable})

        return render(request, self.template_name, {
            'form': form,
            'cable': cable,
            'return_url': self.get_return_url(request, cable),
        })

    def post(self, request, pk=None):
        with transaction.atomic():
            cable = get_object_or_404(Cable, pk=pk)
            form = forms.CommissionForm(request.POST, initial={'cable': cable})

            if form.is_valid():
                form.save()

                return redirect(self.get_return_url(request, cable))

            return render(request, self.template_name, {
                'form': form,
                'cable': cable,
                'return_url': self.get_return_url(request, cable),
            })


class UndoCommissionView(PermissionRequiredMixin, GetReturnURLMixin, View):
    permission_required = 'dcim.edit_cable'
    queryset = Cable.objects.all()
    template_name = 'nautobot_cable_utils/undo_commission.html'

    def get(self, request, pk=None):
        cable = get_object_or_404(Cable, pk=pk)
        form = ConfirmationForm(initial=request.GET)

        return render(
            request,
            self.template_name,
            {
                "obj": cable,
                "form": form,
                "obj_type": self.queryset.model._meta.verbose_name,
                "return_url": self.get_return_url(request, cable),
            },
        )

    def post(self, request, pk=None):
        cable = get_object_or_404(Cable, pk=pk)
        form = ConfirmationForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                cable_new = Cable()
                cable_new.termination_a = cable.termination_a
                cable_new.termination_b = cable.termination_b
                cable_new.status = Status.objects.get(slug="planned")

                cable.delete()
                cable_new.save()

        return redirect(self.get_return_url(request, cable_new))


class DeviceCommissionView(PermissionRequiredMixin, GetReturnURLMixin, View):
    permission_required = 'dcim.edit_cable'
    template_name = 'nautobot_cable_utils/bulk_commission.html'

    def get(self, request, pk=None):
        device = get_object_or_404(Device, pk=pk)

        # set key, if not present
        if 'current_device' not in request.session:
            request.session['current_device'] = None

        if request.session['current_device'] != str(pk):
            cable_list = list()
            for cable in device.get_cables().filter(status__slug="planned"):
                cable_list.append(str(cable.pk))

            request.session['current_device'] = str(pk)
            request.session['cable_list'] = cable_list
            request.session.modified = True

        cable = get_object_or_404(Cable, pk=request.session['cable_list'][0])
        form = forms.CommissionForm(initial={'cable': cable})

        return render(request, self.template_name, {
            'form': form,
            'count': len(request.session['cable_list']),
            'object': cable,
            'verbose_name': Cable._meta.verbose_name,
            'verbose_name_plural': Cable._meta.verbose_name_plural,
            'return_url': self.get_return_url(request, device),
            'active_tab': 'main',
        })

    def post(self, request, pk=None):
        with transaction.atomic():
            device = get_object_or_404(Device, pk=pk)
            cable = get_object_or_404(Cable, pk=request.session['cable_list'][0])
            form = forms.CommissionForm(request.POST, initial={'cable': cable})

            if '_create' in self.request.POST:
                if form.is_valid():
                    request.session['cable_list'].pop(0)
                    request.session.modified = True
                    form.save()
            elif '_skip' in self.request.POST:
                request.session['cable_list'].pop(0)
                request.session.modified = True

            if len(request.session['cable_list']) > 0 and '_cancel' not in self.request.POST:
                if form.is_valid() or '_skip' in self.request.POST:
                    return redirect(request.path)
                else:
                    # re-render page to display ValidationErrors
                    return render(request, self.template_name, {
                        'form': form,
                        'count': len(request.session['cable_list']),
                        'object': get_object_or_404(Cable, pk=request.session['cable_list'][0]),
                        'verbose_name': Cable._meta.verbose_name,
                        'verbose_name_plural': Cable._meta.verbose_name_plural,
                        'return_url': self.get_return_url(request, device),
                        'active_tab': 'main',
                    })

            if 'current_device' in self.request.session.keys():
                del request.session['current_device']
            if 'cable_list' in self.request.session.keys():
                del request.session['cable_list']

        return redirect(self.get_return_url(request, device))


class CableTemplateListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'dcim.view_cable_template'
    queryset = CableTemplate.objects.all()
    filterset = filters.CableTemplateFilterSet
    filterset_form = forms.CableTemplateFilterForm
    table = tables.CableTemplateTable
    action_buttons = ("add", "import")
    template_name = 'nautobot_cable_utils/cable_template_list.html'


class CableTemplateCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'dcim.add_cable_template'
    queryset = CableTemplate.objects.all()
    model_form = forms.CableTemplateForm
    default_return_url = 'plugins:nautobot_cable_utils:cabletemplate_list'
    template_name = "nautobot_cable_utils/cabletemplate_edit.html"


class CableTemplateBulkCreateView(generic.BulkCreateView):
    queryset = CableTemplate.objects.all()
    form = forms.CableTemplateBulkCreateForm
    model_form = forms.CableTemplateBulkForm
    pattern_target = "name"
    template_name = "nautobot_cable_utils/cabletemplate_bulk_add.html"


class CableTemplateEditView(CableTemplateCreateView):
    permission_required = 'dcim.edit_cable_template'


class CableTemplateBulkImportView(BulkImportView):
    queryset = CableTemplate.objects.all()
    model_form = forms.CableTemplateCSVForm
    table = tables.CableTemplateTable


class CableTemplateBulkDeleteView(BulkDeleteView):
    queryset = CableTemplate.objects.all()
    filterset = filters.CableTemplateFilterSet
    table = tables.CableTemplateTable


class MeasurementLogListView(PermissionRequiredMixin, ObjectListView):
    permission_required = 'dcim.view_measurement_log'
    queryset = MeasurementLog.objects.all()
    table = tables.MeasurementLogTable
    action_buttons = tuple()
    template_name = 'nautobot_cable_utils/measurement_log_list.html'


class MeasurementLogCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'dcim.add_measurement_log'
    queryset = MeasurementLog.objects.all()
    model_form = forms.MeasurementLogForm
    default_return_url = 'plugins:nautobot_cable_utils:measurement_log_list'


class MeasurementLogEditView(CableTemplateCreateView):
    permission_required = 'dcim.edit_measurement_log'


class MeasurementLogBulkDeleteView(BulkDeleteView):
    queryset = MeasurementLog.objects.all()
    table = tables.MeasurementLogTable


class CableRouterAddView(PermissionRequiredMixin, FormView):
    permission_required = 'dcim.add_cable'
    template_name = "nautobot_cable_utils/cable_router_add.html"

    termination_types = {
        "interface": ContentType.objects.get_for_model(Interface),
        "front-port": ContentType.objects.get_for_model(FrontPort),
    }

    termination_forms = {
        "interface": CableRouterLinkToInterfaceForm,
        "front-port": CableRouterLinkToFrontPortForm,
    }

    termination_names = {
        'interface': "Interface",
        "front-port": "Front Port",
    }

    termination_a_type = None
    termination_b_type = None
    termination_a_type_name = None
    termination_b_type_name = None
    termination_a = None
    form_class = None

    def dispatch(self, request, *args, **kwargs):
        self.termination_a_type = self.termination_types[kwargs.get("termination_a_type")]
        self.termination_b_type = self.termination_types[kwargs.get("termination_b_type")]
        self.termination_a_type_name = self.termination_names[kwargs.get("termination_a_type")]
        self.termination_b_type_name = self.termination_names[kwargs.get("termination_b_type")]
        self.termination_a = self.termination_a_type.model_class().objects.get(id=kwargs.get("termination_a_id"))
        self.form_class = self.termination_forms[kwargs.get("termination_b_type")]

        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        return {
            **kwargs,
            "termination_a": self.termination_a,
            "termination_a_type": self.termination_a_type,
            "termination_b_type": self.termination_b_type,
        }

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data()

        return {
            **ctx,
            "termination_a_type": self.termination_a_type,
            "termination_b_type": self.termination_b_type,
            "termination_a_type_name": self.termination_a_type_name,
            "termination_b_type_name": self.termination_b_type_name,
            "termination_a": self.termination_a,
        }

    def form_valid(self, form):
        query_params1 = map(lambda cid: f"cable={cid}", form.cleaned_data['path'])
        query_params2 = [
            f"media_type={form.cleaned_data['media_type']}",
            f"termination_a_type={self.termination_a_type.id}",
            f"termination_a_id={self.termination_a.id}",
            f"termination_b_type={self.termination_b_type.id}",
            f"termination_b_id={form.cleaned_data['termination_b_id']}"
        ]
        query_params = "&".join([*query_params1, *query_params2])
        redirect_url = reverse("plugins:nautobot_cable_utils:cable_router_verify") + "?" + query_params
        return HttpResponseRedirect(redirect_url)


class CableRouterVerifyView(PermissionRequiredMixin, FormView):
    permission_required = 'dcim.add_cable'
    form_class = CableRouterVerifyForm
    template_name = "nautobot_cable_utils/cable_router_verify.html"

    def get_cable_path(self):
        ct_termination_a = ContentType.objects.get_for_id(self.request.GET.get("termination_a_type"))
        ct_termination_b = ContentType.objects.get_for_id(self.request.GET.get("termination_b_type"))

        termination_a = ct_termination_a.model_class().objects.get(pk=self.request.GET.get("termination_a_id"))
        termination_b = ct_termination_b.model_class().objects.get(pk=self.request.GET.get("termination_b_id"))

        cable_list = self.request.GET.getlist("cable")
        cable_path = CablePath(termination_a, ct_termination_a, termination_b, ct_termination_b, cable_list)

        return cable_path

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        cable_path = self.get_cable_path()

        needed_cable_table = NeededCableTable(cable_path.get_needed_cables())

        return {
            **ctx,
            'termination_a': cable_path.termination_a,
            "termination_b": cable_path.termination_b,
            "path": cable_path.get_renderable_path(),
            "needed_cable_table": needed_cable_table,
        }

    def form_valid(self, form):
        cable_path = self.get_cable_path()
        needed_cables = cable_path.get_needed_cables()
        planned_status = Status.objects.get(slug=CableStatusChoices.STATUS_PLANNED)

        for needed_cable in needed_cables:
            Cable.objects.create(
                termination_a=needed_cable['termination_a'],
                termination_b=needed_cable['termination_b'],
                status=planned_status,
            )

        messages.success(self.request, f"{len(needed_cables)} Cables were created.")

        return HttpResponseRedirect(cable_path.termination_a.get_absolute_url())
