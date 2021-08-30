from django.views.generic import ListView
from .models import Post


class PostListView(ListView):
    # queryset = Post.published.all()
    model = Post    # == Post.objects.all()
    context_object_name = 'posts'   # the default is object_list

    paginate_by = 3
    template_name = 'blog/post/post_list.html'

