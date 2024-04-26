from django.db import models


class Skills(models.Model):
    class Meta:
        db_table = "Skills"
        verbose_name_plural = "Skills"

    title = models.CharField(
        max_length=200, blank=False, null=False, unique=True
    )

    def __str__(self):
        return f"{self.pk} - {self.title}"
