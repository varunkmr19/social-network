from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import json

class Post(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')
    def __str__(self):
        return self.content
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

#class Comment(models.Model):
#   content = models.TextField()
#   date_created = models.DateTimeField(auto_now_add=True)
#   author = models.ForeignKey(User, on_delete=models.CASCADE)
#   post = models.ForeignKey('Post', on_delete=models.CASCADE)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')
    date_created = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date_created']
    def __str__(self):
        #author = self.user
        return '{} by {}'.format(self.content, self.author)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class Reply(models.Model):
    comment = models.ForeignKey(Comment, related_name='replies',  on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    reply = models.TextField()

    def __str__(self):
        return self.user.username

    @property
    def get_replies(self):
        return self.replies.all()