from django.db import models


class Sample(models.Model):
    image = models.ImageField(upload_to="sample/%Y/%m/%d/")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "sample"
        ordering = ["-created_at"]
