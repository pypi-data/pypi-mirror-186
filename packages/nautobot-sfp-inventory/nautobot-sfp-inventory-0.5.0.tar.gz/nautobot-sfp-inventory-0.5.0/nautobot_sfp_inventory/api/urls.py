from nautobot.core.api import OrderedDefaultRouter
from .views import SFPTypeViewSet, SFPViewSet

router = OrderedDefaultRouter()
router.register("sfp-types", SFPTypeViewSet)
router.register("sfps", SFPViewSet)

app_name = "nautobot_sfp_inventory-api"
urlpatterns = router.urls
