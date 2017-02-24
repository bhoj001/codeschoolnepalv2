from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.posts, name="post-list"),
    url(r'(?P<slug>[\w-]+)/$', views.post_detail, name="post-detail"),

    ]