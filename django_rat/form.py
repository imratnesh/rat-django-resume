from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Field,
                                 Submit, HTML)
from django import forms

from .models import Projects


class AddProjectForm(forms.ModelForm):
    class Meta:
        model = Projects
        fields = ['resume', 'name', 'description', 'started', 'completion']

    def __init__(self, *args, **kwargs):
        super(AddProjectForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        #
        #
        self.helper.layout = Layout(

            Field('resume',
                  autocomplete='off',
                  css_class="search-form-label"
                  ),

            Field('name',
                  autocomplete='off',
                  css_class="search-form-label"
                  ),

            Field('description',
                  autocomplete='off',
                  css_class="search-form-label",
                  ),

            Field('started',
                  autocomplete='off',
                  css_class="search-form-label",
                  ),
            Field('completion',
                  autocomplete='off',
                  css_class="search-form-label",
                  ),
            Field('screenshots',
                  autocomplete='off',
                  css_class="search-form-label",
                  ),

            HTML(""" """),

            Submit('submit', 'Save Project', css_class='upload-btn btn btn-success"')
        )
        #
        #
        self.helper.form_method = 'POST'
