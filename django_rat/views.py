import datetime

from django.http import HttpResponse
from django.views.generic import DeleteView, DetailView, UpdateView, ListView, FormView, TemplateView

from .form import AddProjectForm
from .models import Projects, Resume

# Create your views here.
first = 'Ratnesh Web | '


class HomeIndex(ListView):
    template_name = 'index.html'
    model = Resume
    context_object_name = 'queryset'

    def render_to_response(self, context, **response_kwargs):
        response = super(HomeIndex, self).render_to_response(context, **response_kwargs)
        response.set_cookie("lastLogin", datetime.datetime.now().date())
        # print(response.get('lastLogin'))
        return response

    def get_context_data(self, **kwargs):
        if 'lastLogin' in self.request.COOKIES:
            req = 'Welcome again. You last visited on ' + self.request.COOKIES['lastLogin']
        else:
            req = 'Welcome'
        k = super().get_context_data(projects=Projects.objects.all(), title=f'{first}Home', reqs=req)
        # res = self.render_to_response(**kwargs)
        # res.set_cookie('success', 'sucbb bcess')
        # print(res.get('success'), 'hh')
        return k


class ProjectDetailView(DetailView):
    model = Projects
    template_name = 'project-detail.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f'{first}Project detail')


class MessageView(TemplateView):
    # form_class = AddProjectFormView
    template_name = 'message.html'

    # msg = getattr(MessageView, 'message')
    # print(msg)

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f'{first}Message', message='Added successfully')


class ThesisPdfView(TemplateView):
    template_name = 'thesis.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs, title=f'{first}M.E. Thesis', active='active')


class AddProjectFormView(FormView):
    template_name = 'addProjectForm.html'
    form_class = AddProjectForm
    success_url = '/resume/message'

    # def get(self, request, *args, **kwargs):
    #     signupform = self.form_class()
    #     context = {'addprojectform': signupform, }
    #
    #     return render(request, template_name='addProjectForm.html')
    #
    #
    # def post(self, request, *arsg, **kwargs):
    #     signupform = self.form_class(request.POST)
    #
    #     if signupform.is_valid():
    #         print('VALID')
    #         signupform.save()
    #
    #     context = {'addprojectform': signupform, }

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class EditProjectFormView(UpdateView):
    template_name = 'edit-project.html'
    form_class = AddProjectForm
    model = Projects
    # setattr(MessageView, 'message', 'Updated')

    success_url = '/resume/message'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProjectDeleteView(DeleteView):
    model = Projects
    # form_class = AddProjectFormView
    template_name = 'delete-confirm.html'
    # setattr('message', 'Deleted')
    success_url = '/resume/message'


def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
