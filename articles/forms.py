from django import forms
from .models import Article, Activity

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'description']

class ActivityForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['description', 'file']
