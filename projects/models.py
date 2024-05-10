from enum import unique
from django.db import models

from skills.models import Skills


class Projects(models.Model):
    class Meta:
        db_table = "Projects"
        verbose_name_plural = "Projects"

    title = models.CharField(max_length=200, blank=False, null=False, unique=True)
    description = models.TextField(blank=False, null=False)
    snapshot = models.CharField(max_length=200, blank=False, null=False)
    repository_link = models.URLField(blank=False, null=False)
    start = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)
    skills = models.ManyToManyField(Skills)

    def __str__(self):
        return f"{self.pk} - {self.title}"
