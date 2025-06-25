from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title

class Activity(models.Model):
    article = models.ForeignKey(Article, related_name='activities', on_delete=models.CASCADE)
    description = models.TextField()
    file = models.FileField(upload_to='activities/')

    def __str__(self):
        return f"{self.article.title} - {self.description[:20]}"
