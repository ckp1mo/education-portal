import datetime
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
from lms.models import Course
from users.models import Subscription, User


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


@shared_task()
def deactivate_user():
    """Деактивация пользователя, если не заходил в течении месяца"""
    users = User.objects.filter(is_active=True)
    time_now = datetime.datetime.now(datetime.timezone.utc)
    for user in users:
        if user.last_login:
            date = user.last_login + datetime.timedelta(days=30)
            if date < time_now:
                user.is_active = False
                user.save()
