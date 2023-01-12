from django.db import models

# Create your models here.

class User(models.Model):
    data = models.JSONField()
    class Meta:
        db_table = 'users'