from django.db import models

# Create your models here.
class Tickets(models.Model):
    Resolved_By = models.CharField(max_length=100)
    Status = models.CharField(max_length=50)
    Parent_Record_Type = models.CharField(max_length=50)
    Resolved_DateTime = models.DateField()
    Created_Date_Time = models.DateField()


class File(models.Model):
    file = models.FileField(upload_to='uploads/')