from django.db import models
from django.contrib.auth.models import AbstractUser
from embed_video.fields import EmbedVideoField

# Create your models here.
# index model
class Background(models.Model):
    image = models.ImageField(upload_to="img/%y", null=True)
    description = models.TextField(null=True, blank=False)

class Equipments(models.Model):
    objname = models.CharField(max_length=50)
    image = models.ImageField(upload_to="img/%y", null=True)
    description = models.TextField(null=True, blank=False)

class Footer(models.Model):
    services = models.TextField(null=True, blank=False)
    about = models.TextField(null=True, blank=False)
    gym = models.TextField(null=True, blank=False)

# User Profile Model
class User(AbstractUser):
    name = models.CharField(max_length=30, null=True)
    email = models.EmailField(unique=True, null=True)
    idcardno = models.IntegerField( null=True)
    phoneno = models.IntegerField( null=True)
    image = models.ImageField(upload_to="img/%y", default="avatar.jpeg", null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class Session(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    sl_no = models.IntegerField(unique=True, null=True)
    date = models.DateField()
    duration = models.CharField(max_length=10, null=True, blank=False)
    image = models.ImageField(upload_to="img/%y", null=True, blank=False)

    def __str__(self):
        return str(self.time)
        return str(self.date)

class Video(models.Model):
    title = models.CharField(max_length=100)
    added = models.DateTimeField(auto_now_add=True)
    url = EmbedVideoField()

    def __str__(self):
        return str(self.title)

    class Meta:
        ordering = ['-added']