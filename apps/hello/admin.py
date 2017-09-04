from django.contrib import admin

from .models import Account, WebRequest, Logs

admin.site.register(WebRequest)
admin.site.register(Account)
admin.site.register(Logs)