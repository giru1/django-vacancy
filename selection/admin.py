from django.contrib import admin

from selection.models import Selection


# Register your models here.
@admin.register(Selection)
class SelectionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'owner')  # Поля, которые будут отображаться в списке
    search_fields = ('name',)  # Поля, по которым можно будет искать
    list_filter = ('owner',)  # Фильтры для списка
    ordering = ('id',)  # Сортировка по ID

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.prefetch_related('items')  # Оптимизация запроса для связанных объектов
        return queryset