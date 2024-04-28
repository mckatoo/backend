from django.db import models
from django.utils.text import slugify

from images.models import Images


class Pages(models.Model):
    summernote_fields = "__all__"

    class Meta:
        db_table = "Pages"
        verbose_name_plural = "Pages"

    title = models.CharField(max_length=200, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    slug = models.SlugField(
        max_length=250, null=False, blank=True, unique=True, default=""
    )
    image = models.ForeignKey(
        Images,
        models.SET_NULL,
        blank=True,
        null=True,
    )

    def save(self):
        if not self.pk and self.slug.__len__() < 1:
            self.slug = "".join(slugify(self.title))
        return super().save()

    def __str__(self):
        return f"{self.pk} - {self.slug} - {self.title}"
