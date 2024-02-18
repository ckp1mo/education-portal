from rest_framework import serializers
from users.models import User, Payment, Subscription


class SubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subscription
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'


class PaymentSerializers(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'
