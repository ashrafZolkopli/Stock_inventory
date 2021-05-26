from Product.models import Supplier, Stock
from django.db.models import Sum

supplier = Supplier.objects.get(
    company_name='Ashraf'
)

stock_item = Stock.objects.filter(
    product__supplier=supplier
).values(
    'product__slug',
    'product__name',
).annotate(
    stock=Sum('quantity')
)

print(stock_item)
