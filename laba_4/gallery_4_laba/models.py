from django.db import models

class Cat(models.Model):
    photo = models.ImageField(upload_to='img/')
    description = models.TextField()
    like = models.CharField(max_length=20, default=0)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
