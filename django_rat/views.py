import datetime

from django.http import HttpResponse
from django.views.generic import DeleteView, DetailView, UpdateView, ListView, FormView

from .form import AddProjectForm
from .models import Projects, Resume

# Create your views here.
first = 'Ratnesh Web | '
class HomeIndex(ListView):
    template_name = 'index.html'
    model = Resume
    context_object_name = 'queryset'

    def get_context_data(self, **kwargs):
        return super().get_context_data(projects=Projects.objects.all(), title=f'{first}Home')


class ProjectDetailView(DetailView):
    # template_name = "project-detail.html"
    model = Projects
    template_name = 'project-detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f'{first}Project detail')


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
    template_name = 'delete-confirm.html'
    success_url = '/resume/'


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
