from rest_framework import serializers

from users.models import User, Location


class UserListSerializer(serializers.ModelSerializer):
    locations = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field="name"
    )

    class Meta:
        model = User
        fields = '__all__'


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):

    id = serializers.IntegerField(required=False)
    locations = serializers.SlugRelatedField(
        many=True,
        queryset=Location.objects.all(),  # Укажите queryset для получения местоположений
        slug_field="id"
    )

    class Meta:
        model = User
        fields = '__all__'
        # exclude = ['locations']

    # def is_valid(self, raise_exception=False):
    #     self._locations = self.initial_data.pop('locations', None)
    #     return super().is_valid(raise_exception=raise_exception)


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
