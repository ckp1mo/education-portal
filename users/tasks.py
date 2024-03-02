from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail

from lms.models import Course
from users.models import Subscription


@shared_task
def send_mail_if_update_course(pk):
    """Отправка письма при обновлении курса"""
    course = Course.objects.get(pk=pk)
    subscriptions = Subscription.objects.filter(course=pk)
    if subscriptions:
        for sub in subscriptions:
            send_mail(
                subject='Обновление курса',
                message=f'Курс "{course.title}" был обновлен',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[sub.user.email]
            )


def deactivate_user():
    pass
