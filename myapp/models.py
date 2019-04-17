from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    href = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

class InfoUser(models.Model):
    text = models.TextField(default="Фронтенд разработчик.Так же знаком и с серверной стороной разработки.")
    href = models.TextField(default="https://portfolio-mmrqljtoef.now.sh/")

    def __str__(self):
        return self.text