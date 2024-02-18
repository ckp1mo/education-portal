from rest_framework import serializers

from lms.models import Course, Lesson
from lms.validators import VideoLinkValidator
from users.models import Subscription


class LessonSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [VideoLinkValidator(field='video_link')]


class CourseSerializer(serializers.ModelSerializer):
    lesson_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(source='lesson_set', read_only=True, many=True)
    subscription = serializers.SerializerMethodField()

    def get_subscription(self, obj):
        request = self.context.get('request')
        if request:
            return Subscription.objects.filter(user=request.user, course=obj).exists()
        return False

    def get_lesson_count(self, instance):
        return instance.lesson_set.count()

    class Meta:
        model = Course
        fields = '__all__'

