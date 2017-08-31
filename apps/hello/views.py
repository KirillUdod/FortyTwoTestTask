# Create your views here.
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from .models import WebRequest

import json


class IndexPage(TemplateView):
    template_name = u'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)

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
