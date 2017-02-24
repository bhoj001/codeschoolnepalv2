from courses.models import Course, Category, Lesson
from rest_framework import serializers


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    courses = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='courses_api:course-detail',
        read_only=True
    )
    class Meta:
        model = Category
        fields = (
            'category_name',
            'category_image',
            'category_summary',
            'slug',
            'courses'
        )

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    # course category is related to the course
    category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='courses_api:category-detail'
    )

    # all the lessons
    lessons = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='courses_api:lesson-detail',
        read_only=True
    )

    class Meta:
        model = Course
        fields = (
            'course_name',
            'course_summary',
            'slug',
            'category',
            'lessons'

        )


class LessonSerializer(serializers.ModelSerializer):
    """
    serialize the lesson model
    """
    course = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='courses_api:course-detail',
    )
    class Meta:
        model = Lesson
        fields = ('course', 'lesson_title', 'lesson_video', 'lesson_content')





