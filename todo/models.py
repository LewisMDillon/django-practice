from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=false, blank=false)
    done = models.BooleanField(null=false, blank=false, default_value=false)