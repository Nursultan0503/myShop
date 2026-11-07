from django.contrib import admin
from .models import Product, SerialNumber, ProductComment


class SerialNumberInline(admin.StackedInline):
    model = SerialNumber
    can_delete = False


class ProductCommentInline(admin.TabularInline):
    model = ProductComment
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'category', 'price', 'quantity', 'created_at')
    list_filter = ('category', 'brand')
    search_fields = ('title', 'brand')
    inlines = [SerialNumberInline, ProductCommentInline]


@admin.register(SerialNumber)
class SerialNumberAdmin(admin.ModelAdmin):
    list_display = ('number', 'product', 'warranty_months')
    search_fields = ('number',)


@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'product', 'rating', 'created_at')
    list_filter = ('rating',)
