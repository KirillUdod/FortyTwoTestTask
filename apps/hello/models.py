from django.conf import settings
from django.db import models

from image_cropping import ImageCropField, ImageRatioField


class AccountManager(models.Manager):
    def create_account(self, user, first_name, last_name, birthday, jabber, skype, bio, other_info):
        account = self.model(user=user, first_name=first_name, last_name=last_name,
                             birthday=birthday, jabber=jabber, skype=skype, bio=bio, other_info=other_info)
        account.save(using=self._db)
        return account


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, verbose_name=u'Пользователь', related_name=u'account')

    first_name = models.CharField(u'First Name', max_length=255)
    last_name = models.CharField(u'Last Name', max_length=255)

    birthday = models.DateField(u'Birthday', blank=True, null=True)

    jabber = models.CharField(u'Jabber', max_length=50)
    skype = models.CharField(u'Skype', max_length=50)
    bio = models.TextField('Bio')
    other_info = models.TextField('Other contacts', blank=True, null=True)

    image = ImageCropField(blank=True, upload_to='photo')
    cropping = ImageRatioField('image', '200x200')

    objects = AccountManager()

    class Meta:
        verbose_name = u'Account'
        verbose_name_plural = u'Accounts'

    def __str__(self):
        return self.get_full_name()

    def __unicode__(self):
        return self.get_full_name()

    def get_full_name(self):
        full_name = u'%s %s' % (self.last_name, self.first_name)
        return full_name.strip()


class WebRequest(models.Model):
    request = models.CharField(max_length=500)

    def as_json(self):
            return dict(
                input_id=self.id,
                request=self.request[:50],
            )

    def __str__(self):
        return self.request

    def __unicode__(self):
        return self.request