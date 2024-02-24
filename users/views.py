from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from users.models import User, Payment, Subscription
from users.serializers import UserSerializer, PaymentSerializers, SubscriptionSerializer
from users.services import get_pay


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class UserDeleteAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        amount = serializer.validated_data.get('amount')

        user = self.request.user
        payment = get_pay(amount, user)

        response_data = {
            "id": payment.id,
            "amount": payment.amount,
            "stripe_id": payment.stripe_id
        }

        return Response(response_data)


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson',)
    ordering_fields = ('date',)


class SubscriptionCreateAPIView(generics.CreateAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def perform_create(self, serializer):
        serializer.save()
        self.request.user.subscription_set.add(serializer.instance)


class SubscriptionDestroyAPIView(generics.DestroyAPIView):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()
    permission_classes = [IsAuthenticated]
