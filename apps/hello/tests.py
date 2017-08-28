from django.core.urlresolvers import reverse
from django.test import TestCase, Client

# Create your tests here.


class IndexTests(TestCase):

    def test_index(self):
        "return hard-coded data for the template"
        c = Client()
        response = c.get('/')
        assert(response.content)