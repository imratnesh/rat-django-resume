import datetime

from django.http import HttpResponse
from django.views.generic import DeleteView, DetailView, UpdateView, TemplateView, FormView

from django_rat.models import Projects, Resume
from .form import AddProjectForm


# Create your views here.

class HomeIndex(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(queryset=Resume.objects.all())


class ProjectDetailView(DetailView):
    # template_name = "project-detail.html"
    model = Projects
    template_name = 'project-detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title='Project detail')


class AddProjectFormView(FormView):
    template_name = 'addProjectForm.html'
    form_class = AddProjectForm
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditProjectFormView(UpdateView):
    template_name = 'edit-project.html'
    form_class = AddProjectForm
    model = Projects
    success_url = '/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Projects
    # form_class = AddProjectFormView
    template_name = 'delete_confirm.html'

    success_url = '/resume/'


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)