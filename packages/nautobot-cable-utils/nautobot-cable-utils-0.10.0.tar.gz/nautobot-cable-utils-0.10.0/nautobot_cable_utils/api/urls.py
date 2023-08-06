from nautobot.core.api import OrderedDefaultRouter
from .views import CablePlugViewSet, CableTemplateViewSet

router = OrderedDefaultRouter()
router.register("cable-plug", CablePlugViewSet)
router.register("cable-template", CableTemplateViewSet)

app_name = "nautobot_cable_utils-api"
urlpatterns = router.urls
