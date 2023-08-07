import django_filters
from netbox.filtersets import ChangeLoggedModelFilterSet, NetBoxModelFilterSet
from utilities.filters import ContentTypeFilter
from .models import *
from django.db.models import Q


class PTUEventAssignmentFilterSet(ChangeLoggedModelFilterSet):
    content_type = ContentTypeFilter()
    ptuevent_id = django_filters.ModelMultipleChoiceFilter(
        queryset=PTUEvent.objects.all(),
        label='PTUEvent (ID)',
    )
    relation_id = django_filters.ModelMultipleChoiceFilter(
        queryset=PTUEventRelation.objects.all(),
        label='PTUEvent relation (ID)',
    )
    relation = django_filters.ModelMultipleChoiceFilter(
        field_name='relation__name',
        queryset=PTUEventRelation.objects.all(),
        to_field_name='name',
        label='PTUEvent relation (name)',
    )

    class Meta:
        model = PTUEventAssignment
        fields = ['id', 'content_type_id', 'object_id']


class PTAppSystemFilterSet(NetBoxModelFilterSet):
    class Meta:
        model = PTAppSystem
        fields = ['id', 'name', 'slug', 'tenant', 'description', 'comments']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(
            Q(name__icontains=value) |
            Q(tenant__icontains=value) |
            Q(slug__icontains=value) |
            Q(description__icontains=value) |
            Q(comments__icontains=value)
        )


class PTAppSystemAssignmentFilterSet(ChangeLoggedModelFilterSet):
    content_type = ContentTypeFilter()
    app_system_id = django_filters.ModelMultipleChoiceFilter(
        queryset=PTAppSystem.objects.all(),
        label='PTAppSystem (ID)',
    )

    class Meta:
        model = PTAppSystemAssignment
        fields = ['id', 'content_type_id', 'object_id']
