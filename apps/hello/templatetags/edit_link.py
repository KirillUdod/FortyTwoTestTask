from django import template
from django.core.urlresolvers import reverse

from hello.models import WebRequest

register = template.Library()


def url_to_edit_object(object):
    url = reverse('admin:%s_%s_change' %(object._meta.app_label,  object._meta.model_name),  args=[object.id] )
    return u'<a href="%s"><h4>(admin)</h4></a>' % url


@register.simple_tag
def edit_link(object):
    return url_to_edit_object(WebRequest.objects.order_by('?').first())