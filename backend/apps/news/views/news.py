from ..models import News
from django.views.generic import DetailView, ListView


class NewsListView(ListView):
    """
    Список новостей
    """
    model = News
    queryset = News.objects.filter(is_published=True)
    paginate_by = 6
    template_name = "apps/news/news-list.html"


class NewsDetailView(DetailView):
    """
    Просмотр одной новости
    """
    model = News
    template_name = "apps/news/news-detail.html"
