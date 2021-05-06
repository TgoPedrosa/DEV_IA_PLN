from django.db import models

# Create your models here.
class Preprocess(models.Model):

    sample_id = models.IntegerField(default=0)
    
    y = models.BooleanField()
    x = models.JSONField()