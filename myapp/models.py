from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

# Статьи
class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Текст')
    date = models.DateTimeField(default=timezone.now, verbose_name='Дата')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    href = models.TextField(null=True,blank=True, verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'pk': self.pk})

    class Meta:
        verbose_name_plural= 'Статьи'
        verbose_name = 'Статья'


# Информация об Авторе
class InfoUser(models.Model):
    text = models.TextField(default="Фронтенд разработчик.Так же знаком и с серверной стороной разработки.", verbose_name='Инфо')
    href = models.TextField(default="https://portfolio-mmrqljtoef.now.sh/", verbose_name='ссылка')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural= 'Инфо Автора'
        verbose_name = 'Инфо'