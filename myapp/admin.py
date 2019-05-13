from django.contrib import admin
from .models import Article, InfoUser
# Register your models here.
class AdminArticle(admin.ModelAdmin):
    list_display = ('title', 'content', 'date')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')

admin.site.register(Article, AdminArticle)
admin.site.register(InfoUser)