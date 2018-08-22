from django.db import models

# Create your models here.


class Gallery(models.Model):
    description = models.CharField(default="作品的描述" , max_length=100)
    image =models.ImageField(default="default.png" , upload_to = 'Image/')
    title = models.CharField(default="作品的名称" , max_length=50)

    def __str__(self):
        return self.title
