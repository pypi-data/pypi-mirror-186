import django_tables2 as tables
from netbox.tables import NetBoxTable, columns
from .models import PTUEvent, PTUEventRelation, PTUEventAssignment, PTAppSystem, PTAppSystemAssignment


class PTUEventTable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )
    # default_action = ChoiceFieldColumn()

    class Meta(NetBoxTable.Meta):
        model = PTUEvent
        fields = ('pk', 'name', 'description')
        default_columns = ('name', 'description')


class PTUEventRelationTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = PTUEventRelation
        fields = ('pk', 'name', 'description')
        default_columns = ('name', 'description')


class PTUEventAssignmentTable(NetBoxTable):
    content_type = columns.ContentTypeColumn(
        verbose_name='Object Type'
    )
    object = tables.Column(
        linkify=True,
        orderable=False
    )
    PTUEvent = tables.Column(
        linkify=True
    )
    relation = tables.Column(
        linkify=True
    )
    actions = columns.ActionsColumn(
        actions=('edit', 'delete')
    )

    class Meta(NetBoxTable.Meta):
        model = PTUEventAssignment
        fields = ('pk', 'content_type', 'object',
                  'ptuevent', 'relation', 'actions')
        default_columns = ('pk', 'content_type', 'object',
                           'ptuevent', 'relation')


class AppSystemTable(NetBoxTable):
    name = tables.Column(linkify=True)

    class Meta(NetBoxTable.Meta):
        model = PTAppSystem
        fields = ('pk', 'id', 'name', 'tenant', 'description', 'comments')
        default_columns = ('name', 'description')


class AppSystemAssignmentTable(NetBoxTable):
    content_type = columns.ContentTypeColumn(verbose_name='Object type')
    object = tables.Column(linkify=True, orderable=False)
    app_system = tables.Column(linkify=True)
    actions = columns.ActionsColumn(actions=('edit', 'delete'))

    class Meta(NetBoxTable.Meta):
        model = PTAppSystemAssignment
        fields = ('pk', 'content_type', 'object', 'app_system', 'actions')
        default_columns = ('pk', 'content_type', 'object', 'app_system')
