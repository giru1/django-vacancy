import json
from rest_framework import viewsets, status
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from ads.models import Category, Ads
from ads.permissions import AdsPermission
from ads.serializers import AdsSerializer, CategorySerializer


def index(request):
    return JsonResponse({
        "status": "ok 200"
    })


class AdsDetailView(RetrieveAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]

class AdsCreateView(CreateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]

class AdsUpdateView(UpdateAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [AdsPermission]

class AdsDeleteView(DestroyAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [AdsPermission]

class AdsListView(ListAPIView):
    queryset = Ads.objects.all()
    serializer_class = AdsSerializer
    permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        if cats := request.GET.getlist("cat", None):
            self.queryset = self.queryset.filter(category__in=cats)

        if text := request.GET.get("text", None):
            self.queryset = self.queryset.filter(name__icontains=text)

        if location := request.GET.get("location", None):
            self.queryset = self.queryset.filter(author__user_locations__name__icontains=location)

        if price_from := request.GET.get("price_from", None):
            self.queryset = self.queryset.filter(price__gte=price_from)

        if price_to := request.GET.get("price_to", None):
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().list(request, *args, **kwargs)

@method_decorator(csrf_exempt, name='dispatch')
class AdsImageView(UpdateView):
    model = Ads
    fields = ['image']

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.image = request.FILES.get('image', None)

        self.object.save()

        return JsonResponse({
            "id": self.object.id,
            "name": self.object.name,
            "author": self.object.author.id,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "category": self.object.category.id,
        })

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
