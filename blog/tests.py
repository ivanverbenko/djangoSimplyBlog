from django.http import HttpRequest
from django.urls import resolve
from django.test import TestCase
from .models import Article
from .views import home_page, article_page


class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE'))
        self.assertTrue(html.endswith('</html>'))

    def test_home_page_shows_article(self):
        Article.objects.create(
            title='title test',
            summary='summary test',
            full_text='full test',
            category='cat test'
        )
        request = HttpRequest()
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertIn('title test',html)
        self.assertIn('summary test', html)
        self.assertIn('cat test', html)
        self.assertNotIn('full test',html)
        # получается, что она удаляется сама?хм..
class ArticleModelTest(TestCase):

    def test_article_model_save_and_retrive(self):
        #Проверка на правильность создания модели
        article_1=Article(
            title='art_1',
            full_text='full_text_1',
            summary='summary_1',
            category='category_1',
        )
        article_1.save()
        all_article=Article.objects.all()
        self.assertEqual(article_1.title,all_article[0].title)
        #article_1.delete()#получается, что сохранения при тестах идет только на время тестов?

class ArticlePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        a=Article.objects.create(
            title='title test',
            summary='summary test',
            full_text='full test',
            category='cat test'
        )
        request = HttpRequest()
        response = article_page(request,article_slug=a.slug)#что-то не уверен, что так правильно
        html = response.content.decode('utf8')
        self.assertIn('title test', html)
        self.assertIn('cat test', html)
        self.assertIn('full test', html)
