from django.contrib import admin
from .models import CarMake, CarModel


# Customize how CarModel appears inline within CarMake admin
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1

# CarMake Admin
@admin.register(CarMake)
class CarMakeAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    inlines = [CarModelInline]

# CarModel Admin
@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'make', 'type', 'year', 'created_at')
    list_filter = ('type', 'year', 'make')
    search_fields = ('name',)