from django.db import models

# Create your models here.


class UploadedImage(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='uploads/')
    
