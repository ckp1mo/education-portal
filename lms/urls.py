from django.urls import path
from rest_framework.routers import DefaultRouter
from lms.apps import LmsConfig
from lms.views import CourseViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, LessonUpdateAPIView, \
    LessonDeleteAPIView

app_name = LmsConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
    path('create-lesson/', LessonCreateAPIView.as_view(), name='create-lesson'),
    path('list-lesson/', LessonListAPIView.as_view(), name='list-lesson'),
    path('retrieve-lesson/<int:pk>', LessonRetrieveAPIView.as_view(), name='retrieve-lesson'),
    path('update-lesson/<int:pk>', LessonUpdateAPIView.as_view(), name='update-lesson'),
    path('delete-lesson/<int:pk>', LessonDeleteAPIView.as_view(), name='delete-lesson'),
] + router.urls
