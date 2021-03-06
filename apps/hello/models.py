# -*- coding: utf-8 -*-
from django.conf import settings
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django.db import models

from image_cropping import ImageCropField, ImageRatioField


class AccountManager(models.Manager):
    def create_account(self, user, birthday, jabber, skype, bio,
                       other_info, image):
        account = self.model(user=user,
                             birthday=birthday, jabber=jabber, skype=skype,
                             bio=bio, other_info=other_info,
                             image=image)
        account.save(using=self._db)
        return account


class Account(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                verbose_name=u'Account',
                                related_name=u'account')

    birthday = models.DateField(u'Birthday', blank=True, null=True)

    jabber = models.CharField(u'Jabber', max_length=50, blank=True, null=True)
    skype = models.CharField(u'Skype', max_length=50, blank=True, null=True)
    bio = models.TextField('Bio',  blank=True, null=True)
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
        full_name = u'%s %s' % (self.user.last_name, self.user.first_name)
        return full_name.strip()

    def first_name(self):
        return self.user.first_name

    def last_name(self):
        return self.user.last_name

    def email(self):
        return self.user.email

    def save(self, *args, **kwargs):
        self.user.save()
        super(Account, self).save(*args, **kwargs)


class WebRequest(models.Model):
    request = models.CharField(max_length=500)
    priority = models.IntegerField(default=0)

    def as_json(self):
            return dict(
                input_id=self.id,
                request=self.request[:50],
            )

    class Meta:
        verbose_name = u'Request'
        verbose_name_plural = u'Requests'

    def __str__(self):
        return self.request

    def __unicode__(self):
        return self.request


class Logs(models.Model):
    CHOICES = (
        ('0', 'created'),
        ('1', 'edited'),
        ('2', 'deleted'),
    )

    action = models.CharField(max_length=1, choices=CHOICES)
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Log'
        verbose_name_plural = u'Logs'

    def __unicode__(self):
        return 'qq'

    def __str__(self):
        return "%s %s is %s" % (self.content_object.__class__.__name__,
                                self.object_id,
                                self.CHOICES[int(self.action)][1])
