from django.db import models

class Profile(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100)
    linkedin = models.URLField(max_length=200)
    instagram = models.URLField(max_length=200)
    github = models.URLField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return f'{self.first_name} {self.middle_name} {self.last_name}'
