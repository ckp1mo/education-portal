from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from users.apps import UsersConfig
from users.views import PaymentCreateAPIView, PaymentListAPIView, UserCreateAPIView, UserListAPIView, \
    UserRetrieveAPIView, UserUpdateAPIView, UserDeleteAPIView, SubscriptionCreateAPIView, SubscriptionDestroyAPIView

app_name = UsersConfig.name

urlpatterns = [
    path('payment/create/', PaymentCreateAPIView.as_view(), name='payment_create'),
    path('payment/list/', PaymentListAPIView.as_view(), name='payment_list'),
    # авторизация
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # user CRUD
    path('create/', UserCreateAPIView.as_view(), name='user_create'),
    path('list/', UserListAPIView.as_view(), name='user_list'),
    path('retrieve/<int:pk>', UserRetrieveAPIView.as_view(), name='user_retrieve'),
    path('update/<int:pk>', UserUpdateAPIView.as_view(), name='user_update'),
    path('delete/<int:pk>', UserDeleteAPIView.as_view(), name='user_delete'),
    # подписка
    path('subscription_create/', SubscriptionCreateAPIView.as_view(), name='sub_create'),
    path('subscription_delete/<int:pk>', SubscriptionDestroyAPIView.as_view(), name='sub_delete'),
]
