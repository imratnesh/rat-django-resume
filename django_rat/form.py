from django import forms
from .models import Resume, Projects


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['resume','name', 'description', 'started', 'completion']
