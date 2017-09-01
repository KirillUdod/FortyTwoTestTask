from django import forms
from .models import Account


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
