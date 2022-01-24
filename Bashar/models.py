from django.db import models


# Create your models here.
class Shipper(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    from_star = models.CharField(max_length=30)
    image = models.FilePathField('./img')


