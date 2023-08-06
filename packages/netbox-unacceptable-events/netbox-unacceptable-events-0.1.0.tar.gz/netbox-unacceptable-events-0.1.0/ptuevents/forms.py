from netbox.forms import NetBoxModelForm
from pyrsistent import v
from .models import PTUEvent, PTUEventRelation, PTUEventAssignment, PTAppSystem, PTAppSystemAssignment
from utilities.forms.fields import CommentField
from utilities.forms import (
    BootstrapMixin, DynamicModelChoiceField)
from django import forms


class PTUEventForm(NetBoxModelForm):
    class Meta:
        model = PTUEvent
        fields = ('name', 'description', 'comments')


class PTUEventRelationForm(NetBoxModelForm):
    class Meta:
        model = PTUEventRelation
        fields = ('name', 'description')


class PTUEventAssignmentForm(BootstrapMixin, forms.ModelForm):
    ptuevent = DynamicModelChoiceField(
        queryset=PTUEvent.objects.all()
    )
    relation = DynamicModelChoiceField(
        queryset=PTUEventRelation.objects.all()
    )

    class Meta:
        model = PTUEventAssignment
        fields = (
            'ptuevent', 'relation',
        )


class PTAppSystemForm(NetBoxModelForm):
    comments = CommentField()

    class Meta:
        model = PTAppSystem
        fields = ('name', 'slug', 'tenant', 'description', 'comments', 'tags')


class PTAppSystemAssignmentForm(BootstrapMixin, forms.ModelForm):
    app_system = DynamicModelChoiceField(queryset=PTAppSystem.objects.all())

    class Meta:
        model = PTAppSystemAssignment
        fields = ('app_system',)
