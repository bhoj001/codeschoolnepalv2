from django.db import models


class Category(models.Model):
    """Different category of courses"""

    category_name = models.CharField('Course Category name', max_length=255)
    category_image = models.ImageField("Category Image 350X230", upload_to="category")
    category_summary = models.CharField("Category Summary", default="", max_length=255)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.category_name


class Course(models.Model):
    created_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, related_name="courses", on_delete=models.CASCADE)
    course_name = models.CharField('Course Name', max_length=255)
    course_summary = models.CharField(max_length=255)
    course_image = models.ImageField("Course Image 350X230", upload_to='course')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.course_name

    def get_absolute_url(self):
        return 'hello'


class Lesson(models.Model):
    """Course Lesson"""
    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    lesson_title = models.CharField(max_length=255)
    lesson_content = models.TextField()
    lesson_video = models.URLField("Youtube Video Link")

    def __str__(self):
        return self.lesson_title
