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

    def create(self, validated_data):
        locations_data = validated_data.pop('locations', [])
        user = User.objects.create(**validated_data)

        # Сохраняем местоположения
        user.locations.set(locations_data)
        user.set_password(validated_data["password"])  # Убедитесь, что пароль устанавливается правильно
        user.save()

        return user

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
