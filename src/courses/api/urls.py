from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = format_suffix_patterns([
    # Course model Urls
    url(r'courses/$', views.CourseListView.as_view(), name="course-list"),
    # course detail page
    url(r'course/(?P<pk>\d+)/$', views.CourseDetailView.as_view(), name="course-detail"),
    # Category list
    url(r'categories/$', views.CategoryListView.as_view(), name="category-list"),
    # Category detail
    url(r'category/(?P<pk>\d+)/$', views.CategoryDetailView.as_view(), name="category-detail"),
    # lessons
    url(r'lessons/$', views.LessonListView.as_view(), name='lesson-list'),
    # api/lesson/
    url(r'lesson/(?P<pk>\d+)/$', views.LessonDetailView.as_view(), name='lesson-detail'),


])