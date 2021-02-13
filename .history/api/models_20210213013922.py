from django.db import models
from django.contrib.auth.models import User


class StoryData(models.Model):
    TypeChoices = ('Image', 'Image'), ('Video', 'Video')
    photo = models.FileField()
    type = models.CharField(max_length=255,choices=TypeChoices)


class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    instagram_id = models.CharField(max_length=255)
    facebook_id = models.CharField(max_length=255)
    gender = models.CharField(max_length=255)
    friends = models.ManyToManyField(User, related_name='Friends')
    profile_image = models.ImageField()
    # story = models.ManyToManyField(Story, related_name='Story')
    def __str__(self):
        return self.name

class Story(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    story = models.ManyToManyField(StoryData, related_name='Story')

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='sender')

    receiver = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='receiver')
           
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    def __str__(self):
        return self.message
    
    class Meta:
        ordering = ['timestamp']
        

