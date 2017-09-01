# Create your views here.
from django.views.generic import FormView, TemplateView, View
from django.http import HttpResponse
from django.shortcuts import redirect

import json

from .models import Account, WebRequest
from .forms import EditForm


class IndexPage(TemplateView):
    template_name = u'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        #context[u'account'] = self.request.user.account
        context[u'account'] = Account.objects.all().first()
        # context[u'account'] = {'first_name': 'My first name',
        #                        'last_name': 'My last name',
        #                        'birthday': 'date of my b',
        #                        'email': 'email',
        #                        'jabber': '22345',
        #                        'skype': 'my_skype',
        #                        'bio': 'bio',
        #                        'other_info': 'other',
        #                        }
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
        acc = Account.objects.all().first()
        self.user = Account.objects.all().first().user
        return {'first_name': acc.first_name,
                'last_name': acc.last_name,
                'birthday': acc.birthday,
                'email': acc.email,
                'skype': acc.skype,
                'jabber': acc.jabber,
                'other_info': acc.other_info,
                'bio': acc.bio,
            }

    def get_context_data(self, **kwargs):
        if self.request.method == "GET":
            context = super(EditView, self).get_context_data(**kwargs)
            context[u'account'] = self.request.user.account
            return context
        else:
            print('edited')
            print(self.request.POST.get('data'))
            context = super(EditView, self).get_context_data(**kwargs)
            context[u'account'] = self.request.user.account
            return context


    def get_form_kwargs(self):
        kwargs = super(EditView, self).get_form_kwargs()
        kwargs.update({u'user': self.user})
        return kwargs