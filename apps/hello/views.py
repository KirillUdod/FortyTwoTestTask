# Create your views here.
from django.views.generic import TemplateView, View
from django.http import HttpResponse

import json

from .models import Account, WebRequest

class IndexPage(TemplateView):
    template_name = u'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)
        #context[u'account'] = self.request.user.account
        context[u'account'] = {'first_name': 'My first name',
                               'last_name': 'My last name',
                               'birthday': 'date of my b',
                               'email': 'email',
                               'jabber': '22345',
                               'skype': 'my_skype',
                               'bio': 'bio',
                               'other_info': 'other',
                               }
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
