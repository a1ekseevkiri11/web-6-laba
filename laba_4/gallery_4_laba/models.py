from django.db import models

class Product(models.Model):
    photo = models.ImageField(upload_to='img/')
    name = models.CharField(max_length=200, db_index=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        
    def __str__(self):
        return self.name


class Captcha(models.Model):
    key = models.CharField(max_length=50, unique=True)
    answer = models.CharField(max_length=10)