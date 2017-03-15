from django.shortcuts import render
from django.shortcuts import HttpResponse, get_object_or_404
from .forms import ContactUsForm
from .models import Category, Course
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
import json
from django.core import serializers


def index(request):
    data = dict()
    data['categories'] = Category.objects.all()
    return render(request, 'homepage.html', data)


def categories(request):
    """Display all the course categories in one page with search button """
    data = dict()
    # Display all the categories of courses
    categories = Category.objects.all()
    data['categories'] = categories
    data['categories'] = categories
    return render(request, 'courses/category/categories.html', data)


def category_detail(request, slug):
    "Display the detail of a category"
    data = dict()
    category = get_object_or_404(Category, slug=slug)
    courses = category.courses.all()
    data['category'] = category
    data['courses'] = courses
    return render(request, 'courses/category/category_detail.html', data)


def course_detail(request, slug):
    """Serve the detail description of course"""
    data = dict()
    course = get_object_or_404(Course, slug=slug)
    data['course'] = course
    lessons = course.lessons.all()
    data['lessons'] = lessons
    print(lessons)
    return render(request, 'courses/course/course_detail.html', data)


def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            email = form.cleaned_data['email']
            # suscribe = form.cleaned_data('suscribe')
            send_mail(name, message, 'surfer.manoj@gmail.com', ['manojit.gautam@gmail.com'], fail_silently=True)
            contact_message = True
            return render(request, 'contact.html', {'form': ContactUsForm(), message: contact_message})
        else:
            # return the form with binding values
            return render(request, 'contact.html', {'form': form})
    else:
        # Blank empty form
        form = ContactUsForm()
        return render(request, 'contact.html', {'form': form})


def course_ajax_search(request):
    if request.method == "POST":
        search_text = request.POST.get('search_text')
        # Full text search
        if len(search_text) < 2:
            return HttpResponse(" ")

        courses = Course.objects.filter(
            course_name__contains=search_text
        )
        print(courses)
        courses = serializers.serialize(
            'json', courses, fields=('slug', 'course_name',)
        )
        return HttpResponse(courses, content_type="application/json")
    else:
        return HttpResponseRedirect("/courses")
