from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(
        auto_now_add=True, null=False, blank=False
    )

    @classmethod
    def create(cls, title, description):
        page = cls(title=title, description=description)
        return page
