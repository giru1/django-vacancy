from rest_framework import serializers

from ads.models import Ads, Category
from selection.models import Selection


class SelectionSerializer(serializers.ModelSerializer):
    items = serializers.PrimaryKeyRelatedField(many=True, queryset=Ads.objects.all())

    class Meta:
        model = Selection
        fields = ['id', 'name', 'owner', 'items']