from django.db import models


class Images(models.Model):

    class Meta:
        db_table = "Images"
        verbose_name_plural = "Images"

    url = models.CharField(max_length=300, null=False, blank=False) 
    alt = models.CharField(max_length=300, null=False, blank=False) 

    def __str__(self):
        return f"{self.pk} - {self.alt} - {self.url}"
