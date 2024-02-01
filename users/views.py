from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from users.models import User, Payment
from users.serializers import UserSerializer, PaymentSerializers


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentCreateAPIView(generics.CreateAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializers
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson',)
    ordering_fields = ('date',)
