from django.db import models


# Create your models here.
class MainInfo(models.Model):
    name = models.CharField(u'Name', max_length=50)
    last_name = models.CharField(u'Last Name', max_length=50)
    birthday = models.DateField(u'Birthday')
    email = models.EmailField(u'Email')
    jabber = models.CharField(u'Jabber', max_length=50)
    skype = models.CharField(u'Skype', max_length=50)
    bio = models.TextField('Bio')
    other_info = models.TextField('Other contacts', blank=True, null=True)


class WebRequest(models.Model):
    request = models.CharField(max_length=500)

    def as_json(self):
            return dict(
                input_id=self.id,
                request=self.request[:50],
            )
