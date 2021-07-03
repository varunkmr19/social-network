from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from PIL import Image
import json

class Post(models.Model):
    image = models.ImageField(blank=True, null=True, upload_to='post_image')
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    #likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, default=None, related_name='dislikes')
    shared_body  = models.TextField(blank=True, null=True)
    shared_on = models.DateTimeField(blank=True, null=True)
    shared_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name='+')
    likes = models.ManyToManyField(User, related_name='like', default=None, blank=True)
    like_count = models.BigIntegerField(default='0')
    class Meta:
        ordering = ['-date_posted']#, '-shared_on']
    def __str__(self):
        return self.content
    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name='author')
    date_created = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')
    parent = models.ForeignKey('self', blank=True, on_delete=models.CASCADE, null=True, related_name='+')

    class Meta:
        ordering = ['date_created']
    def __str__(self):
        #author = self.user
        return '{} by {}'.format(self.content, self.author)
    @property
    def children(self):
        return Comment.objects.filter(parent=self).order_by("date_created").all()
    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    followers = models.ManyToManyField(User, blank=True, related_name='followers')
    verified = models.BooleanField(default=False)
    followers_count = models.BigIntegerField(default='0')
    def __str__(self):
        return f'{self.user.username} Profile'
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

