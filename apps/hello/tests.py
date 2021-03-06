from django.contrib.auth import get_user_model
from django.test import TestCase, Client

import datetime

from .models import Account, Logs

User = get_user_model()


class IndexTests(TestCase):

    def test_index(self):
        "\return hard-coded data for the template"
        u1 = User.objects.create(username='user1',
                                 first_name='Testname',
                                 last_name='Test lastname')
        Account.objects.create(user=u1,
                               birthday=datetime.date.today(),
                               jabber='test_jadder',
                               bio='asdas')
        c = Client()
        response = c.get('/')
        assert response.content


class TestAccountModel(TestCase):

    def setUp(self):
        u1 = User.objects.create(username='user1',
                                 first_name='Testname',
                                 last_name='Test lastname')
        Account.objects.create(user=u1,
                               birthday=datetime.date.today(),
                               jabber='test_jadder',
                               bio='asdas')

    def test_model(self):
        "check saved data for right value"
        main = Account.objects.get(user__first_name="Testname")
        self.assertEqual(main.birthday, datetime.date.today())
        self.assertEqual(main.jabber, 'test_jadder')
        self.assertEqual(main.bio, 'asdas')


class TestLogsModel(TestCase):
    def setUp(self):
        u1 = User.objects.create(username='user1',
                                 first_name='Testname',
                                 last_name='Test lastname')
        a1 = Account.objects.create(user=u1,
                                    birthday=datetime.date.today(),
                                    jabber='test_jadder',
                                    bio='asdas')
        self.uid = a1.id

    def test_logs(self):
        "test logs model for creation"
        log = Logs.objects.filter(object_id=self.uid)
        assert log
