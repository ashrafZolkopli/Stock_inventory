from django.contrib import admin
from django.contrib.admin import filters
from .models import (
    Supplier,
    Product,
    ProductImage,
    Stock
)
# Register your models here.


class ProductImageStackInline(admin.StackedInline):
    model = ProductImage


class StockTabularInline(admin.TabularInline):
    model = Stock


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = [
        'supplier__company_name',
        'created_by__first_name'
    ]

    inlines = [
        ProductImageStackInline,
        StockTabularInline,
    ]

    fieldsets = (
        (None, {
            'fields': ('name', 'spec', 'slug',)
        }),
        ('Admin Info', {
            'classes': ('collapse',),
            'fields': ('supplier', ('created_by', 'created')),
        }),
    )

    readonly_fields = [
        'slug',
        'created_by',
        'created',
    ]

    raw_id_fields = [
        'supplier',
        'created_by',
    ]


class ProductTabularInline(admin.TabularInline):
    model = Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    inlines = [
        ProductTabularInline
    ]

    list_filter = [
        'company_name',
        'created_by__first_name'
    ]

    fieldsets = (
        (None, {
            'fields': (('company_name', 'slug'), 'address')
        }),
        ('Contact Info', {
            'classes': ('collapse',),
            'fields': (('contact_person', 'contact_no')),
        }),
        ('Admin Info', {
            'classes': ('collapse',),
            'fields': (('created_by', 'created')),
        }),
    )

    readonly_fields = [
        'created',
        'slug'
    ]
