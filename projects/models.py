from django.db import models
from django.utils.timezone import now

from skills.models import Skills


class Projects(models.Model):
    class Meta:
        db_table = "Projects"
        verbose_name_plural = "Projects"

    title = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    snapshot = models.CharField(max_length=200, blank=False, null=False)
    repository_link = models.URLField(blank=False, null=False)
    start = models.DateField()
    last_update = models.DateField()
    skills = models.ManyToManyField(Skills)

    def save(self, *args, **kargs):
        if not self.start:
            self.start = now()
        return super(Projects, self).save(*args, **kargs)

    def __str__(self):
        return self.title.__str__()
