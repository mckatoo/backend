from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from projects.models import Projects


class ProjectsModelAdmin(SummernoteModelAdmin):
    summernote_fields = "__all__"


admin.site.register(Projects, ProjectsModelAdmin)
