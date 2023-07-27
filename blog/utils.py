




menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    def get_user_context(self, **kwargs):
        context=kwargs
        context['menu']=menu
        return context
