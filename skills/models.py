from django.db import models
from django.forms import model_to_dict


class Skills(models.Model):
    class Meta:
        db_table = "Skills"
        verbose_name_plural = "Skills"

    title = models.CharField(max_length=200, blank=False, null=False, unique=True)

    def __str__(self):
        return self.title.__str__()

    def __json__(self):
        return model_to_dict(self)
