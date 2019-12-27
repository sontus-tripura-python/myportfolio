from django.db import models
from django.utils import timezone
# Create your models here.
class about(models.Model):
    name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    text = models.TextField()
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    linkdin = models.URLField(blank=True)
    image = models.ImageField(upload_to='leaderpics', blank=True)

    def __str__(self):
        return self.name
