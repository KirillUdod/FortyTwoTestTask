from django.contrib import admin

from .models import Account, WebRequest

admin.site.register(WebRequest)
admin.site.register(Account)