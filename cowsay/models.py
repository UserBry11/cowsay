from django.db import models


class Author(models.Model):
    text = models.CharField(max_length=50, blank=True)
