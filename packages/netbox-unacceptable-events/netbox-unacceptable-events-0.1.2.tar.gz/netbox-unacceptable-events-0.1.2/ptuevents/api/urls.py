from netbox.api.routers import NetBoxRouter
from . import views

app_name = 'ptuevents'

router = NetBoxRouter()
router.register('ptuevents', views.PTUEventListViewSet)
router.register('ptueventrelation', views.PTUEventRelationListViewSet)
router.register('ptueventassignment', views.PTUEventAssignmentViewSet)
router.register('pt-app-systems', views.PTAppSystemViewSet)
router.register('pt-app-system-assignment', views.PTAppSystemAssignmentViewSet)

urlpatterns = router.urls

# print(router.urls)
