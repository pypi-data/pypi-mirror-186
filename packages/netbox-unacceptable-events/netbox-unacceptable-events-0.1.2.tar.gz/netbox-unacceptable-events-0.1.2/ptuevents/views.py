from netbox.views import generic
from . import forms, models, tables
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


class PTUEventView(generic.ObjectView):
    queryset = models.PTUEvent.objects.all()


class PTUEventListView(generic.ObjectListView):
    queryset = models.PTUEvent.objects.all()
    table = tables.PTUEventTable
    # actions = ('add', 'export')


class PTUEventEditView(generic.ObjectEditView):
    queryset = models.PTUEvent.objects.all()
    form = forms.PTUEventForm


class PTUEventDeleteView(generic.ObjectDeleteView):
    queryset = models.PTUEvent.objects.all()


# PTPTUEvent relation


class PTUEventRelationView(generic.ObjectView):
    queryset = models.PTUEventRelation.objects.all()


class PTUEventRelationListView(generic.ObjectListView):
    queryset = models.PTUEventRelation.objects.all()
    table = tables.PTUEventRelationTable


class PTUEventRelationEditView(generic.ObjectEditView):
    queryset = models.PTUEventRelation.objects.all()
    form = forms.PTUEventRelationForm


class PTUEventRelationDeleteView(generic.ObjectDeleteView):
    queryset = models.PTUEventRelation.objects.all()


# #
# # PTUEvent assignments
# #

class PTUEventAssignmentEditView(generic.ObjectEditView):
    queryset = models.PTUEventAssignment.objects.all()
    form = forms.PTUEventAssignmentForm
    template_name = 'ptuevents/ptuevent_assignment_edit.html'

    def alter_object(self, instance, request, args, kwargs):
        if not instance.pk:
            # Assign the object based on URL kwargs
            content_type = get_object_or_404(
                ContentType, pk=request.GET.get('content_type'))
            instance.object = get_object_or_404(
                content_type.model_class(), pk=request.GET.get('object_id'))
        return instance

    def post(self, request, *args, **kwargs):
        form = forms.PTUEventAssignmentForm(request.POST)
        if form.is_valid():
            content_type_id = request.GET.get('content_type', -1)
            object_id = request.GET.get('object_id', -1)
            ptuevent = form.cleaned_data['ptuevent']
            qs = models.PTUEventAssignment.objects.filter(
                content_type=content_type_id, object_id=object_id, ptuevent=ptuevent.id)
            if qs.exists():
                redirect_url = request.GET.get('return_url', '/')
                return HttpResponseRedirect(redirect_url)

        return super().post(request, *args, **kwargs)


class PTUEventAssignmentDeleteView(generic.ObjectDeleteView):
    queryset = models.PTUEventAssignment.objects.all()


class PTAppSystemView(generic.ObjectView):
    queryset = models.PTAppSystem.objects.all()

    def get_extra_context(self, request, instance):
        print(self)
        print(request)
        print(instance.id)
        app_system_assignments = models.PTAppSystemAssignment.objects.filter(
            app_system=instance)
        assignments_table = tables.AppSystemAssignmentTable(
            app_system_assignments)
        assignments_table.columns.hide('app_system')
        assignments_table.configure(request)
        content_type_id = ContentType.objects.get_for_model(
            model=models.PTAppSystem).id
        PTUEvent_ass = models.PTUEventAssignment.objects.filter(
            object_id=instance.id, content_type=content_type_id)
        PTUEvents = []
        for r in PTUEvent_ass:
            PTUEvents.append({
                'assignment_id': r.id,
                'name': r.ptuevent,
                'rel': r.relation.name
            })

        return {
            'assignments_table': assignments_table,
            'PTUEvents': PTUEvents
        }


class PTAppSystemListView(generic.ObjectListView):
    queryset = models.PTAppSystem.objects.all()
    table = tables.AppSystemTable


class PTAppSystemEditView(generic.ObjectEditView):
    queryset = models.PTAppSystem.objects.all()
    form = forms.PTAppSystemForm


class PTAppSystemDeleteView(generic.ObjectDeleteView):
    queryset = models.PTAppSystem.objects.all()


class PTAppSystemAssignmentEditView(generic.ObjectEditView):
    queryset = models.PTAppSystemAssignment.objects.all()
    form = forms.PTAppSystemAssignmentForm
    template_name = 'ptuevents/appsystem_assignment_edit.html'

    def alter_object(self, instance, request, args, kwargs):
        if not instance.pk:
            # Assign the object based on URL kwargs
            content_type = get_object_or_404(
                ContentType, pk=request.GET.get('content_type'))
            instance.object = get_object_or_404(
                content_type.model_class(), pk=request.GET.get('object_id'))
        return instance

    def get_extra_addanother_params(self, request):
        return {
            'content_type': request.GET.get('content_type'),
            'object_id': request.GET.get('object_id'),
        }

    def post(self, request, *args, **kwargs):
        form = forms.PTAppSystemAssignmentForm(request.POST)
        if form.is_valid():
            content_type_id = request.GET.get('content_type', -1)
            object_id = request.GET.get('object_id', -1)
            s = form.cleaned_data['app_system']
            qs = models.PTAppSystemAssignment.objects.filter(
                content_type=content_type_id, object_id=object_id, app_system=s.id)
            if qs.exists():
                redirect_url = request.GET.get('return_url', '/')
                return HttpResponseRedirect(redirect_url)

        return super().post(request, *args, **kwargs)


class PTAppSystemAssignmentDeleteView(generic.ObjectDeleteView):
    queryset = models.PTAppSystemAssignment.objects.all()
