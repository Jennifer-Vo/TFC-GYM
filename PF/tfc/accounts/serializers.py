from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator

from accounts.forms import RegisterForm
from accounts.models import UserProfile


class SignupSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=UserProfile.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = UserProfile
        fields = ('username', 'password', 'password2',
                  'email', 'first_name', 'last_name', 'phone_number', 'avatar')
        extra_kwargs = {
          'first_name': {'required': True},
          'last_name': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = UserProfile.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            phone_number=validated_data['phone_number'],
            avatar=validated_data['avatar']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username",  "password", "first_name", "last_name", "email", "phone_number", "avatar"]
        read_only_fields = ["username"]  # we can also specify a list of fields to be read only (not editable)
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'avatar': {'required': False}
        }

    def update(self, instance, validated_data):
        instance.first_name = validated_data['first_name']
        instance.last_name = validated_data['last_name']
        instance.email = validated_data['email']
        instance.phone_number = validated_data['phone_number']
        print(validated_data)
        if 'avatar' in validated_data.keys():
            print("avatar changed")
            instance.avatar = validated_data['avatar']
        if 'password' in validated_data.keys():
            print("password changed")
            instance.set_password(validated_data['password'])
        instance.save()
        return instance


class RestrictedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["username", "first_name", "last_name", "email", "phone_number", "avatar"]
        read_only_fields = ["username", "first_name", "last_name", "email", "phone_number", "avatar"]


class EnrolSerializer(serializers.Serializer): # noqa
    class_id = serializers.IntegerField()
    instance_id = serializers.IntegerField(required=False)

    def validate(self, attrs):
        if not isinstance(int(attrs['class_id']), int) and not isinstance(int(attrs['instance_id']), int):
            raise serializers.ValidationError({"not int"})
        return attrs
