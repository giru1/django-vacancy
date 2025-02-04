from django.http import JsonResponse
import json

from django.http import JsonResponse
# Create your views here.
from django.views.generic import UpdateView, DeleteView
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView

from users.models import User, Location
from users.serializers import UserDetailSerializer, UserListSerializer, UserCreateSerializer, LocationSerializer, UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserCreateView(CreateAPIView):
    model = User
    serializer_class = UserCreateSerializer

    def post(self, request, *args, **kwargs):
        user = UserCreateSerializer(data=json.loads(request.body))
        if user.is_valid():
            user.save()
            return JsonResponse(user.data, status=201)  # Возвращаем статус 201 при успешном создании
        return JsonResponse(user.errors, status=400)  # Возвращаем ошибки с статусом 400


class UserUpdateView(UpdateView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserDeleteView(DeleteView):
    model = User
    success_url = "/"

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)

        return JsonResponse({"status": "ok"}, status=200)


class LocationViewSet(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class Logout(APIView):
    def post(self, request, *args, **kwargs):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)