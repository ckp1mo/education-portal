from django.contrib.auth.models import AbstractUser
from django.db import models
from lms.models import Lesson, Course, NULLABLE


class UserRole(models.TextChoices):
    USER = 'user', 'пользователь'
    MODERATOR = 'moderator', 'модератор'


class User(AbstractUser):
    username = None
    phone = models.CharField(max_length=30, verbose_name='Телефон', **NULLABLE)
    town = models.CharField(max_length=100, verbose_name='Город', **NULLABLE)
    avatar = models.ImageField(upload_to='users/', verbose_name='Аватар', **NULLABLE)
    email = models.EmailField(unique=True, verbose_name='Email')
    role = models.CharField(max_length=9, choices=UserRole.choices, default=UserRole.USER)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return f'{self.email}: {self.first_name}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Payment(models.Model):
    payment_variant = [
        ('cash', 'Наличные'),
        ('card', 'Картой'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(auto_now=True, verbose_name='Дата платежа')
    lesson = models.ForeignKey(Lesson, related_name='lesson', on_delete=models.CASCADE, verbose_name='Урок', **NULLABLE)
    course = models.ForeignKey(Course, related_name='course', on_delete=models.CASCADE, verbose_name='Курс', **NULLABLE)
    payment = models.PositiveIntegerField(verbose_name='Сумма платежа')
    payment_method = models.CharField(max_length=30, choices=payment_variant, default='card', verbose_name='Способ оплаты')

    stripe_id = models.CharField(max_length=300, verbose_name='stripe_id', **NULLABLE)

    def __str__(self):
        return f'{self.user}, {self.lesson if self.lesson else self.course}, {self.date}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='курс')

    def __str__(self):
        return f'{self.user}, {self.course}'

    class Meta:
        verbose_name = 'подписка'
        verbose_name_plural = 'подписки'
