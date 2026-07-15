from django.db import models

# Create your models here.
class Students(models.Model):
    name=models.CharField()
    age=models.IntegerField()
    phone_no=models.IntegerField()

    def __str__(self)->str:
        return self.name