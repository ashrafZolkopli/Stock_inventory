from django.db import models
from django.db.models.aggregates import Sum


class SupplierQuerySet(models.QuerySet):
    pass


class ProductQuerySet(models.QuerySet):
    pass


class ProductImageQuerySet(models.QuerySet):
    pass


class StockQuarySet(models.QuerySet):

    def total_stock_by_product(self, product):
        total = self.filter(product=product).aggregate(stock=Sum('quantity'))
        return total['stock']
