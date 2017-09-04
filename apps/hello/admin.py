from django.contrib import admin

from .models import Account, WebRequest, Logs


class WebRequestAdmin(admin.ModelAdmin):
    list_filter = ('priority', )

admin.site.register(Account)
admin.site.register(Logs)
admin.site.register(WebRequest, WebRequestAdmin)
