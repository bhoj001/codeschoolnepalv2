from django.conf.urls import url
from .views import index
from . import views

urlpatterns = [
 #/course/course_detail_page
 url(r'(?P<slug>[\w-]+)/$', views.course_detail, name="course_detail"),
]