from django.contrib import admin
from .models import Article, Activity

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = ('article', 'description', 'file')
