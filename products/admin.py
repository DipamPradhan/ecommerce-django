from django.contrib import admin
from .models import Product, Review


# Register your models here.
class ReviewInline(admin.TabularInline):
    model = Review
    extra = 0


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ReviewInline,
    ]
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
admin.site.register(Review)
