from django.contrib import admin
from .models import RequestSession, ApiSession
import waffle
from .enums import AlastriaAuthSwitches


class RequestSessionAdmin(admin.ModelAdmin):
    model = RequestSession

    def get_model_perms(self, request):

        if not waffle.switch_is_active(AlastriaAuthSwitches.auth.value):
            return {}

        return super(RequestSessionAdmin, self).get_model_perms(request)


class ApiSessionAdmin(admin.ModelAdmin):
    model = ApiSession

    def get_model_perms(self, request):

        if not waffle.switch_is_active(AlastriaAuthSwitches.auth.value):
            return {}

        return super(ApiSessionAdmin, self).get_model_perms(request)


admin.site.register(RequestSession, RequestSessionAdmin)
admin.site.register(ApiSession, ApiSessionAdmin)
