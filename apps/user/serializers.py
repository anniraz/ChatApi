from rest_framework import serializers

from apps.user.models import User

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "email",
                  "phone_number",
                  "age",
                  "bio",
                  "image",
                  "is_online",
                  "last_action",
                  )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "email",
                  "phone_number",
                  "age",
                  "bio",
                  "image",
                  'password',
                "last_action",
                "is_online",
                  )

        read_only_fields=('last_action','is_online',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user