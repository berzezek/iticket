from iticket.api.views import TicketViewSet, EventViewSet, OrderViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tickets', TicketViewSet, basename='ticket')
router.register(r'events', EventViewSet, basename='event')
router.register(r'orders', OrderViewSet, basename='order')

urlpatterns = router.urls