from pages.models import Pages
from django_summernote.admin import SummernoteModelAdmin

from django.contrib import admin


class PagesModelAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Pages, PagesModelAdmin)
