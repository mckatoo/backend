from django.db import models


class Pages(models.Model):
    class Meta:
        db_table = "Pages"

    url = models.CharField(
        max_length=100, blank=False, null=False, default="", unique=True
    )
    title = models.CharField(
        max_length=200, null=False, blank=False, default=""
    )
    description = models.TextField(null=False, blank=False, default="")
