from django.db import models

# Create your models here.
from django.db import models
 
# Create your models here.
class datas(models.Model):
    titile=models.CharField(max_length=100)
    day_travel=models.IntegerField()
    budget=models.IntegerField()
    detail=models.TextField()

    class Meta:
        db_table="tbdatas"