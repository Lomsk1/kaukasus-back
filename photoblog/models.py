from django.db import models
import os

class Gallery(models.Model):
    title = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(default="./gallery/gallery_default.jpg", upload_to="./gallery")



class Photos(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, blank=False, null=False)
    title = models.CharField(max_length=200, blank=False, default="")
    image = models.ImageField(default="./photo-blog/photo-blog_default.jpg", upload_to="./photo-blog")

def img_delete(image, *args, **kwargs):
    if os.path.isfile(image):
        os.remove(image)
