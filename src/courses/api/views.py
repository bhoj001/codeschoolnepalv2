"""
viewset.py file for api
api v1.0
"""

# Required to create class based view
from rest_framework.views import APIView
# Required to set the http status in response object
from rest_framework import status
# Required to create response object
from rest_framework import response
from rest_framework.response import Response
# course app models
from ..models import Course, Category, Lesson
# courses app serializers
from . import serializers
from django.http import Http404


class CategoryListView(APIView):
    """
    List all the course categories
    """
    def get(self,request, format=None):
        categories = Category.objects.all()
        serializer = serializers.CategorySerializer(categories, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetailView(APIView):
    """
    Get the detail of a category
    """

    def get_object(self, pk):
        try:
            category = Category.objects.get(pk=pk)
            return category
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Category = self.get_object(pk)
        serializer = serializers.CourseSerializer(Category, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Category = self.get_object(pk)
        serializer = serializers.CourseSerializer(Category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CourseListView(APIView):
    """
    List all the course
    """

    def get(self, request, format=None):
        courses = Course.objects.all()
        context = {'request': request}
        serializer = serializers.CourseSerializer(courses, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.CourseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CourseDetailView(APIView):
    """
    Display the details of course
    """
    def get_object(self, pk):
        try:
            course = Course.objects.get(pk=pk)
            return course
        except Course.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = serializers.CourseSerializer(course, context={'request':request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        course = self.get_object(pk)
        serializer = serializers.CourseSerializer(course, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        course = self.get_object(pk)
        course.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LessonListView(APIView):
    """
    List all the lessons
    """

    def get(self, request, format=None):
        lessons = Lesson.objects.all()
        context = {'request': request}
        serializer = serializers.LessonSerializer(lessons, many=True, context={'request':request})
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = serializers.LessonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LessonDetailView(APIView):
    """
    Display the details of a lesson
    """
    def get_object(self, pk):
        try:
            lesson = Lesson.objects.get(pk=pk)
            return lesson
        except Lesson.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        lesson = self.get_object(pk)
        serializer = serializers.LessonSerializer(lesson, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        lesson = self.get_object(pk)
        serializer = serializers.LessonSerializer(
            lesson,
            data=request.data,
            context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        lesson = self.get_object(pk)
        lesson.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)