from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from lms.models import Course, Lesson
from users.models import User, Subscription


class InitialTestCase(APITestCase):
    """ Создание тестового пользователя, курса, урока, подписки """

    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create(email='test@test.com', password='qwerty')
        self.client.force_authenticate(user=self.user)

        self.course = Course.objects.create(
            title='Test course',
            description='Test description'
        )

        self.lesson = Lesson.objects.create(
            title='Test lesson',
            description='Test',
            course=self.course,
            owner=self.user
        )

        self.subscription = Subscription.objects.create(
            user=self.user,
            course=self.course
        )


class LessonTestCase(InitialTestCase):
    def test_create_lesson(self):
        """ Тестирование создания урока """
        data = {
            'title': 'Test lesson2',
            'description': 'Test description2',
            'course': self.course.id
        }

        response = self.client.post(
            '/create-lesson/', data=data,
        )
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertTrue(Course.objects.all().exists())

    def test_list_lesson(self):
        """ Тестирование просмотр списка уроков """
        response = self.client.get(
            '/list-lesson/',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_retrieve_lesson(self):
        """ Тестирование вывода одного урока """
        response = self.client.get(
            f'/retrieve-lesson/{self.lesson.id}',
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_lesson(self):
        data = {'title': 'Test lesson update'}

        response = self.client.patch(
            f'/update-lesson/{self.lesson.id}',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        self.assertEqual(
            response.json()['title'],
            'Test lesson update'
        )

    def test_delete_lesson(self):

        response = self.client.delete(
            f'/delete-lesson/{self.lesson.id}',
        )

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class SubscriptionTestCase(InitialTestCase):
    """ Тесты удаления и создания подписки """

    def test_create_subscription(self):
        """ Тест создания подписки """
        data = {
            "user": self.user.id,
            "course": self.course.id,
        }
        response = self.client.post(
            '/user/subscription_create/',
            data=data,
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
        self.assertTrue(Subscription.objects.all().exists())

    def test_delete_subscription(self):
        """ Тест удаления подписки """

        response = self.client.delete(
            f'/user/subscription_delete/{self.subscription.id}',
        )
        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )
