from django.contrib import admin

from mailer.models import Mailer


class CustomMailerAdmin(admin.ModelAdmin):
    readonly_fields = [field.name for field in Mailer._meta.get_fields()]

    def has_add_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    def changeform_view(self, request, object_id=None, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save_and_continue'] = False
        extra_context['show_save'] = False
        return super(CustomMailerAdmin, self).changeform_view(request, object_id, extra_context=extra_context)

admin.site.register(Mailer, CustomMailerAdmin)
