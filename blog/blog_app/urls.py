# here is URLS

from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name="home"),
    path('post/new/', PostCreateView.as_view(), name="new-post"),
    path('user/<str:username>', UserPostListView.as_view(), name="user-post"),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update', ProjectUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete', ProjectDeleteView.as_view(), name='post-delete'),
    path('about', views.about, name="about")
]

# here class based view is just more than function is views.py and it consider specific types of
# html page. like <app>/<model>_<view_type>.html
# Class-based views provide an  way to implement views as Python objects instead of functions.
# They do not replace function-based views,
