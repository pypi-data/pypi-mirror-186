from django.contrib import admin
from .models import RequestSession, ApiSession


class RequestSessionAdmin(admin.ModelAdmin):
    model = RequestSession


class ApiSessionAdmin(admin.ModelAdmin):
    model = ApiSession


admin.site.register(RequestSession, RequestSessionAdmin)
admin.site.register(ApiSession, ApiSessionAdmin)
