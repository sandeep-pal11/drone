from django.contrib import admin
from .models import Product, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_on_sale']  # Specify fields to display in the admin list view
    list_filter = ['category', 'is_on_sale']  # Add 'is_on_sale' to enable filtering by sale status
    search_fields = ['name', 'category']  # Allow searching by name and category

# Register the Product model with the custom admin configuration
admin.site.register(Product, ProductAdmin)
admin.site.register(Order)