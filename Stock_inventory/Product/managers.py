from django.db import models
from .query_sets import (
    SupplierQuerySet,
    ProductQuerySet,
    ProductImageQuerySet,
    StockQuarySet
)


class SupplierManager(models.Manager):
    def get_queryset(self):
        return SupplierQuerySet(
            self.model,
            using=self._db
        ).select_related(
            'created_by'
        ).prefetch_related(
            'supplier_product'
        )


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(
            self.model,
            using=self._db
        ).select_related(
            'supplier',
            'created_by'
        ).prefetch_related(
            'product_productimage',
            'stock_product'
        )


class ProductImageManager(models.Manager):
    def get_queryset(self):
        return ProductImageQuerySet(
            self.model,
            using=self._db
        ).select_related(
            'product',
            'created_by'
        )


class StockManager(models.Manager):
    def get_queryset(self):
        return StockQuarySet(
            self.model,
            using=self._db
        ).select_related(
            'product',
        )

    def total_stock(self, product):
        return self.get_queryset().total_stock_by_product(product)
