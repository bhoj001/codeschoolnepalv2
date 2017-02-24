from django.conf.urls import url
from . import views
from rest_framework import routers



urlpatterns = [
    # Display all the course related to the course categories
    # /courses/
    url(r'^$', views.categories, name="categories"),
    # /courses/course_category/
    # Category detail page
    # /courses/robotics/
    url(r'(?P<slug>[\w-]+)/$', views.category_detail, name="category_detail"),
]



