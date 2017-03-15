from django.conf.urls import url
from . import views
from rest_framework import routers



urlpatterns = [
    # Display all the course related to the course categories
    # /courses/
    url(r'^$', views.categories, name="categories"),
    # url for course ajax
    url(r'^ajax/$', views.course_ajax_search, name="course_ajax_search"),
    # /courses/course_category/
    # Category detail page
    url(r'^(?P<slug>[\w-]+)/$', views.category_detail, name="category_detail"),

]



