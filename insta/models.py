from django.db import models

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete = models.CASCADE)
    image = models.ImageField(upload_to='images/')
    caption = models.TextField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.caption
