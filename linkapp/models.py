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
    occupants_count = models.ManyToManyField(User)
    police_contact = PhoneNumberField()
    health_contact = PhoneNumberField()

    @classmethod
    def get_all_neighborhoods(cls):
        neighborhoods = cls.objects.all()
        return neighborhoods

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
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

    def save_bs(self):
        self.save()

    def delete_bs(self):
        self.delete()

    @classmethod
    def get_all_bs(cls):
        businesses = cls.objects.all()
        return businesses

    @classmethod
    def get_hood_bs(cls, neighborhood):
        hood_bs = Business.objects.filter(neighborhood__pk = neighborhood)
        return hood_bs

    @classmethod
    def get_profile_bs(cls, profile):
        profile_bs = Business.objects.filter(user__pk = user)
        return profile_bs

class Post(models.Model):
    title = models.CharField(max_length=30)
    description = HTMLField(max_length=70)
    post_user = models.OneToOneField(User,on_delete=models.CASCADE, primary_key=True)
    post_location = models.ForeignKey(Neighborhood, related_name="posts", on_delete=models.CASCADE)
    post_pic = ImageField(manual_crop ='1920x1080')

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()

    @classmethod
    def get_all_posts(cls):
        posts = cls.objects.all()
        return posts

    @classmethod
    def get_hood_posts(cls, neighborhood):
        hood_posts = Post.objects.filter(neighborhood__pk = neighborhood)
        return hood_posts

    @classmethod
    def get_profile_posts(cls, profile):
        profile_posts = Post.objects.filter(user__pk = user)
        return profile_posts




