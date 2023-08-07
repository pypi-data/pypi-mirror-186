from .serializers import PTAppSystemSerializer, PTAppSystemAssignmentSerializer
from netbox.api.viewsets import NetBoxModelViewSet
from ..models import PTUEventRelation, PTUEvent, PTUEventAssignment, PTAppSystem, PTAppSystemAssignment
from .serializers import PTUEventRelationSerializer, PTUEventSerializer, PTUEventAssignmentSerializer
from .. import filtersets


class PTUEventListViewSet(NetBoxModelViewSet):
    queryset = PTUEvent.objects.prefetch_related('tags')
    serializer_class = PTUEventSerializer


class PTUEventRelationListViewSet(NetBoxModelViewSet):
    queryset = PTUEventRelation.objects.prefetch_related('tags')
    serializer_class = PTUEventRelationSerializer


class PTUEventAssignmentViewSet(NetBoxModelViewSet):
    queryset = PTUEventAssignment.objects.prefetch_related(
        'object', 'ptuevent', 'relation')
    serializer_class = PTUEventAssignmentSerializer
    filterset_class = filtersets.PTUEventAssignmentFilterSet


class PTAppSystemViewSet(NetBoxModelViewSet):
    queryset = PTAppSystem.objects.prefetch_related('tenant', 'tags')
    serializer_class = PTAppSystemSerializer
    filterset_class = filtersets.PTAppSystemFilterSet


class PTAppSystemAssignmentViewSet(NetBoxModelViewSet):
    queryset = PTAppSystemAssignment.objects.prefetch_related(
        'object', 'app_system')
    serializer_class = PTAppSystemAssignmentSerializer
    filterset_class = filtersets.PTAppSystemAssignmentFilterSet
