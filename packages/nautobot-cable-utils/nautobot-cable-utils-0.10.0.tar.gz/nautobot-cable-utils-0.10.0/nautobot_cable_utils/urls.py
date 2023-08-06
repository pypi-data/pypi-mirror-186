from __future__ import unicode_literals

from django.urls import path

from . import views

app_name = 'nautobot_cable_utils'
urlpatterns = [
    path(r'reconnect/<uuid:pk>/edit/', views.ReconnectView.as_view(), name='reconnect'),
    path(r'commission/<uuid:pk>/edit/', views.CommissionView.as_view(), name='commission'),
    path(r'undo_commission/<uuid:pk>/edit/', views.UndoCommissionView.as_view(), name='undo_commission'),
    path(r'device_commission/<uuid:pk>/edit/', views.DeviceCommissionView.as_view(), name='device_commission'),
    path(r'cable_templates/', views.CableTemplateListView.as_view(), name='cabletemplate_list'),
    path(r'cable_templates/add/', views.CableTemplateCreateView.as_view(), name='cabletemplate_add'),
    path(r'cable_templates/bulk-add/', views.CableTemplateBulkCreateView.as_view(), name='cabletemplate_bulk_add'),
    path(r'cable_templates/import/', views.CableTemplateBulkImportView.as_view(), name='cabletemplate_import'),
    path(r'cable_templates/delete/', views.CableTemplateBulkDeleteView.as_view(), name='cabletemplate_bulk_delete'),
    path(r'cable_templates/edit/<uuid:pk>', views.CableTemplateEditView.as_view(), name='cabletemplate_edit'),
    path(r'measurement_logs/', views.MeasurementLogListView.as_view(), name='measurement_log_list'),
    path(r'measurement_logs/add/', views.MeasurementLogCreateView.as_view(), name='measurement_log_add'),
    path(r'measurement_logs/delete/', views.MeasurementLogBulkDeleteView.as_view(), name='measurement_log_bulk_delete'),
    path(r'measurement_logs/edit/<uuid:pk>', views.MeasurementLogEditView.as_view(), name='measurement_log_edit'),
    path(r'cable_router/link/<str:termination_a_type>/<uuid:termination_a_id>/to/<str:termination_b_type>', views.CableRouterAddView.as_view(), name='cable_router_link'),
    path(r'cable_router/verify/', views.CableRouterVerifyView.as_view(), name='cable_router_verify')
]
