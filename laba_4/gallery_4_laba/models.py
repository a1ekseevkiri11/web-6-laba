from django.db import models

class Cat(models.Model):
    title = models.CharField(max_length=128)
    photo = models.ImageField(upload_to='img/')
    description = models.TextField()
    like = models.CharField(max_length=20, default=0)

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    def __str__(self):
        information = "\nTitle: "+str(self.title)
        return information
