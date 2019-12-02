from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User
from tinymce.models import HTMLField
from pyuploadcare.dj.models import ImageField


# Create your models here.
class Neighborhood(models.Model):
    neighborhood_name = models.CharField(max_length=30)
    neighborhood_location = models.CharField(max_length=30)
    neighborhood_pic = ImageField(blank=True, manual_crop="1920x1080")
    occupants_count = models.IntegerField(null=True)
    police_contact = PhoneNumberField()
    health_contact = PhoneNumberField()

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    neighborhood = models.ManyToManyField(Neighborhood)
    email = models.EmailField()
    profile_pic = ImageField(manual_crop ='1080x1080')
    bio = HTMLField()

class Business(models.Model):
    bs_name = models.CharField(max_length=30)
    about = HTMLField()
    bs_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    bs_location = models.ForeignKey(Neighborhood, related_name="businesses", on_delete=models.CASCADE)
    bs_email = models.EmailField()
    bs_pic = ImageField(manual_crop ='1920x1080')

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField(max_length=70)
    post_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    post_location = models.ForeignKey(Neighborhood, related_name="posts", on_delete=models.CASCADE)
    post_pic = ImageField(manual_crop ='1920x1080')






