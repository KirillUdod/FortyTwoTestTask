# Create your views here.
from django.views.generic import TemplateView

class IndexPage(TemplateView):
    template_name = u'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexPage, self).get_context_data(**kwargs)

        return context
