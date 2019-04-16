from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='images')

    def __str__(self):
        return f"Проифиль пользователя {self.user.username}"

    def save(self, *args, **kwargs):
        super(Profile, self).save(*args, **kwargs)

        image = Image.open(self.img.url)
        if image.height > 512 or image.width > 512:
            size = (512, 512)
            image.thumbnail(size)
            image.save()