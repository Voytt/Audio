
from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length = 100)
    sub_title = models.CharField(max_length = 100)
    image = models.ImageField(default='card_images/default.jpg', upload_to = 'card_images')
    price = models.FloatField()
    description = models.TextField()
    tag = models.ManyToManyField(Tag)


    def __str__(self):
        return self.name