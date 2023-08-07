from attr import fields
from graphene import ObjectType
from netbox.graphql.types import NetBoxObjectType
from netbox.graphql.fields import ObjectField, ObjectListField
from . import filtersets
from .models import PTUEvent, PTUEventRelation, PTUEventAssignment, PTAppSystem, PTAppSystemAssignment


class PTUEventType(NetBoxObjectType):
    class Meta:
        model = PTUEvent
        fields = '__all__'


class PTUEventRelationType(NetBoxObjectType):
    class Meta:
        model = PTUEventRelation
        fields = '__all__'


class PTUEventAssingmentType(NetBoxObjectType):
    class Meta:
        model = PTUEventAssignment
        fields = '__all__'
        filterset_class = filtersets.PTUEventAssignmentFilterSet


class PTAppSystemType(NetBoxObjectType):
    class Meta:
        model = PTAppSystem
        fields = '__all__'


class PTAppSystemAssignmentType(NetBoxObjectType):
    class Meta:
        model = PTAppSystemAssignment
        fields = '__all__'
        filterset_class = filtersets.PTAppSystemAssignmentFilterSet


class Query(ObjectType):
    ptuevent = ObjectField(PTUEventType)
    ptuevent_list = ObjectListField(PTUEventType)
    relation = ObjectField(PTUEventRelationType)
    relation_list = ObjectListField(PTUEventRelationType)
    ptuevent_assignment = ObjectField(PTUEventAssingmentType)
    ptuevent_assignment_list = ObjectListField(PTUEventAssingmentType)
    ptapp_system = ObjectField(PTAppSystemType)
    ptapp_system_list = ObjectListField(PTAppSystemType)
    ptapp_system_assignment = ObjectField(PTAppSystemAssignmentType)
    ptapp_system_assignment_list = ObjectListField(PTAppSystemAssignmentType)


schema = Query
