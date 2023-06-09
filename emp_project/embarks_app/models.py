from django.db import models
#
# # Create your models here.
class Crud(models.Model):
    slno=models.IntegerField()
    Item_name=models.CharField(max_length=250)
    Description=models.TextField()
