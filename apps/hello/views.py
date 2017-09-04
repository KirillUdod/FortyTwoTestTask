# Create your views here.
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model, login, logout
from django.http import HttpResponse
from django.views.generic import FormView, TemplateView, View
from django.shortcuts import redirect

import json

from .models import Account, WebRequest
from .forms import EditForm, LoginForm

User = get_user_model()


class IndexPage(TemplateView):
    template_name = u'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        context[u'account'] = Account.objects.all().first()
        return context


class RequestsPage(TemplateView):
    template_name = u'requests.html'

    def get_context_data(self, **kwargs):
        context = super(RequestsPage, self).get_context_data(**kwargs)
        context['list'] = WebRequest.objects.all().order_by('-id')[:10]
        return context


class JsonResponse(HttpResponse):
    """
        JSON response
    """
    def __init__(self, content, mimetype='application/json',
                 status=None, content_type=None):
        super(JsonResponse, self).__init__(
            content=json.dumps(content),
            mimetype=mimetype,
            status=status,
            content_type=content_type,
        )


class NewRequestsView(View):
    def get(self, request, **kwargs):
        context = {}
        if request.method == 'GET':
            context['data'] = [ob.as_json() for ob in
                               WebRequest.objects.all().order_by('-id')[:10]]
            return JsonResponse(context)


class EditView(FormView):
    template_name = u'edit_account.html'
    form_class = EditForm
    success_url = '/'

    def get_initial(self):
        # FIXME: change to right way
        self.account = Account.objects.all().first()
        self.user = Account.objects.all().first().user
        return {'first_name': self.account.first_name,
                'last_name': self.account.last_name,
                'birthday': self.account.birthday,
                'email': self.account.email,
                'skype': self.account.skype,
                'jabber': self.account.jabber,
                'other_info': self.account.other_info,
                'bio': self.account.bio
                }

    def form_valid(self, form):
        first_name, last_name, birthday, skype, jabber, other_info, bio = (
            form.cleaned_data.get(u'first_name'),
            form.cleaned_data.get(u'last_name'),
            form.cleaned_data.get(u'birthday'),
            form.cleaned_data.get(u'skype'),
            form.cleaned_data.get(u'jabber'),
            form.cleaned_data.get(u'other_info'),
            form.cleaned_data.get(u'bio')
        )
        self.account.user.first_name = first_name
        self.account.user.last_name = last_name
        self.account.birthday = birthday
        self.account.skype = skype
        self.account.jabber = jabber
        self.account.other_info = other_info
        self.account.bio = bio
        if 'photo' in self.request.FILES:
                self.account.photo = self.request.FILES['photo']
        self.account.save()
        return redirect(reverse(u'edit'))

    def get_context_data(self, **kwargs):
        context = super(EditView, self).get_context_data(**kwargs)
        context[u'account'] = self.request.user.account
        return context

    def get_form_kwargs(self):
        kwargs = super(EditView, self).get_form_kwargs()
        kwargs.update({u'user': self.user})
        return kwargs


class LoginView(FormView):

    template_name = u'login.html'
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect(reverse(u'index'))
        return super(LoginView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.login(self.request)
        if user:
            login(self.request, user)
            return redirect(reverse(u'index'))
        else:
            return redirect(reverse(u'index'))

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        return context


class LogOut(View):
    def get(self, request):
        return self.post(request)

    def post(self, request):
        logout(request)
        return redirect(reverse(u'index'))
