from django.contrib import admin
from .models import Category, Product

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_filter = ('available', 'category')
    list_editable = ('available', 'price')
    search_fields = ('name', 'description')

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)