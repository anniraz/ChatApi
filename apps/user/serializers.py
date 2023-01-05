from rest_framework import serializers

from apps.user.models import User

class UsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "age",
                  "image",
                  "is_online",
                  "last_action",
                  )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id",
                  "username",
                  "age",
                  "image",
                  'password',

                  )

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user