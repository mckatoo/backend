from django.db import models


class Mailer(models.Model):
    class Meta:
        db_table = "Messages"
        verbose_name_plural = "Messages"

    _from = models.CharField(
        max_length=300, null=False, blank=False, db_column="from"
    )
    message = models.TextField(null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        message = self.message if len(self.message) < 30 else self.message[:30] + " ..."
        return f"{self.pk} - {self._from} - {message}"
