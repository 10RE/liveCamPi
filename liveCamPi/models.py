from django.db import models

# Create your models here.
class Camera(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.name