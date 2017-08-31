from django.test import TestCase, Client

import datetime

from .models import MainInfo
# Create your tests here.


class IndexTests(TestCase):

    def test_index(self):
        "return hard-coded data for the template"
        c = Client()
        response = c.get('/')
        assert(response.content)


class TestModel(TestCase):

    def setUp(self):
        MainInfo.objects.create(name='Testname',
                                last_name='Test lastname',
                                birthday=datetime.date.today(),
                                email='test@test.com',
                                jabber='test_jadder',
                                bio='asdas',)

    def test_model(self):
        "check saved data for right value"
        main = MainInfo.objects.get(name="Testname")

        self.assertEqual(main.last_name, 'Test lastname')
        self.assertEqual(main.birthday, datetime.date.today())
        self.assertEqual(main.email, 'test@test.com')
        self.assertEqual(main.jabber, 'test_jadder')
        self.assertEqual(main.bio, 'asdas')
