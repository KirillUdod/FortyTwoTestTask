# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth import get_user_model, authenticate

from .models import Account

User = get_user_model()


class EditForm(forms.ModelForm):
    first_name = forms.CharField(label=u'Name', required=True,
                                 widget=forms.TextInput(attrs={
                                     u'type': u'text',
                                     u'class': u'form-control'
                                 }))

    last_name = forms.CharField(label=u'Last Name', required=True,
                                widget=forms.TextInput(attrs={
                                    u'type': u'text',
                                    u'class': u'form-control'
                                }))

    birthday = forms.DateField(label=u'Date of birth', required=True,
                               widget=forms.TextInput(attrs={
                                   u'type': u'text',
                                   u'class': u'form-control datepicker'
                               }))

    email = forms.CharField(label=u'Email', required=True,
                            widget=forms.TextInput(attrs={
                                u'type': u'text',
                                u'class': u'form-control'
                            }))

    jabber = forms.CharField(label=u'Jabber', required=True,
                             widget=forms.TextInput(attrs={
                                 u'type': u'text',
                                 u'class': u'form-control'
                             }))

    skype = forms.CharField(label=u'Skype', required=True,
                            widget=forms.TextInput(attrs={
                                u'type': u'text',
                                u'class': u'form-control'
                            }))

    bio = forms.CharField(label=u'Bio', required=True,
                          widget=forms.Textarea(attrs={
                              u'type': u'text',
                              u'class': u'form-control',
                              u'rows': '3',

                          }))

    other_info = forms.CharField(label=u'Other contacts', required=True,
                                 widget=forms.Textarea(attrs={
                                     u'type': u'text',
                                     u'class': u'form-control',
                                     u'rows': '3',
                                 }))

    photo = forms.ImageField(label=u'Photo',
                             required=False,
                             widget=forms.FileInput(
                                 attrs={'class': 'form-control'}))

    class Meta:
        model = Account
        fields = (u'first_name', u'last_name', u'birthday', u'email', u'skype',
                  u'jabber', u'bio', u'other_info', u'photo')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(EditForm, self).__init__(*args, **kwargs)


class LoginForm(forms.Form):
    name = forms.CharField(label=u'Логин', required=True,
                           widget=forms.TextInput(attrs={
                               u'type': u'login',
                               u'class': u'form-control col-sm-10'
                           }))
    password = forms.CharField(label=u'Пароль', required=True,
                               widget=forms.PasswordInput(attrs={
                                   u'type': u'password',
                                   u'class': u'form-control col-sm-10'
                               }))

    def clean(self):
        username = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. "
                                        "Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('name')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user
