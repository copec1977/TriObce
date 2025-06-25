from django.test import TestCase
from .models import Article

class ArticleModelTest(TestCase):
    def test_create_article(self):
        article = Article.objects.create(title='Test', description='Desc')
        self.assertEqual(str(article), 'Test')
