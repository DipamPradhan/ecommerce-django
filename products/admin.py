from django.contrib import admin
from .models import Product


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "seller",
        "price",
        "stock",
        "created_at",
    )
    search_fields = ("name",)
    list_filter = (
        "created_at",
        "seller",
    )


admin.site.register(Product, ProductAdmin)
