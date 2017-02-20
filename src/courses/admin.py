from django.contrib import admin
from .models import Course, Category, Lesson

class CourseInline(admin.StackedInline):
    model = Course

class LessonInline(admin.StackedInline):
    model = Lesson

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    inlines = [CourseInline]
    prepopulated_fields = {"slug": ("category_name",),}

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['course_name']
    inlines = [LessonInline]
    prepopulated_fields = {'slug': ("course_name",),}




# Register your models here.
