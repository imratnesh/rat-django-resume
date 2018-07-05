from django import forms

from .models import Projects


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['resume','name', 'description', 'started', 'completion']
