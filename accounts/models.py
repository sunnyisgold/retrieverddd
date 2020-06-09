from django.db import models

# Create your models here.


class Account(models.Model):
    name = models.CharField(max_length=200)
    photo_url = models.URLField()

    age = models.PositiveIntegerField(default=0)

    class Meta:
        db_table = 'user'