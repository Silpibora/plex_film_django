from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Cast(models.Model):
    name = models.CharField(max_length=100)
    character = models.CharField(max_length=100)
    cast_image= models.ImageField(upload_to='cast_images/', default='fallback.jpg')


    def __str__(self):
        return self.name

class Movie(models.Model):
    id=models.AutoField(primary_key=True)
    user=models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField()
    poster1 = models.ImageField(default='fallback.jpg')
    poster2 = models.ImageField(default='fallback.jpg')
    cast= models.ManyToManyField(Cast, blank=True)

    def __str__(self):
        return self.title

