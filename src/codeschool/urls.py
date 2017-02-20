"""codeschool URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.contrib.flatpages import views
import courses.views
from django.contrib import flatpages



urlpatterns = [
    # codeschool nepal homepage
    # Admin urls
    url(r'^admin/', admin.site.urls),
    # Course related urls
    url(r'^$', courses.views.index, name="index"),
    # /courses/
    url(r'^courses/', include('courses.urls',namespace="courses"),),
    # course only url
    # /course/
    url(r'course/', include('courses.course_urls', namespace="course")),
    # contact page
    url(r'^contact/$', courses.views.contact, name="contact"),
    # About page is served from the flat pages
    url(r'about/$', flatpages.views.flatpage, {'url':'/about/'}, name="about")
    # url(r'about/$', name="about")
]

# Append this flatpages_urls at the  last
flatpages_urls = [
    url(r'^about/$', views.flatpage, {'url': '/about/'}, name='about'),
]

if not settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Serving media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
