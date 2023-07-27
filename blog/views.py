from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView

from blog.forms import CommentForm, AddPostForm
from blog.models import Article, Comment
from blog.utils import DataMixin

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]
class HomePage(DataMixin,ListView):
    model = Article
    template_name = 'blog/index.html'
    context_object_name = 'articles'
    def get_context_data(self, *, object_list=None, **kwargs):
        context=super().get_context_data(**kwargs)
        c_def=self.get_user_context(title='Main Page')
        context=dict(list(context.items())+list(c_def.items()))
        return context


class ArticalPage(DataMixin,DetailView):
    model = Article
    template_name = 'blog/article.html'
    context_object_name = 'article'
    slug_url_kwarg = 'article_slug'

    def get_context_data(self, *, object_list=None , **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['article'].title)
        context = dict(list(context.items()) + list(c_def.items()))
        context['form'] = CommentForm()
        context['comments']=Comment.objects.filter(post_id='1')
        return context

    def post(self, request, article_slug):
        post = get_object_or_404(Article, slug=article_slug)
        form = CommentForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('home')

def home_page(*args):
    pass

def about_page(request):
    return render(request,'blog/about.html', {'menu': menu, 'title': 'О сайте'})

def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()
    return render(request, 'blog/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление статьи'})

class RegisterUser(DataMixin,CreateView):
    form_class = UserCreationForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context=super(RegisterUser, self).get_context_data(**kwargs)
        c_def=self.get_user_context(title='Регистрация')
        return dict(list(context.items())+list(c_def.items()))



class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'blog/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data()
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home')

