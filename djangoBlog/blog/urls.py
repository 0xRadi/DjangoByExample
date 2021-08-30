from django.urls import path
from . import views, view_class_based

app_name = 'blog'

urlpatterns = [
    # path('', views.post_list, name='post_list'),
    path('', view_class_based.PostListView.as_view(), name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_details, name='post_detail'),

]