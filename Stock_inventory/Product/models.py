from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from . import managers
# Create your models here.

User = get_user_model()


def get_sentinel_user():
    return User.objects.get_or_create(username='Deleted User')[0]


class Supplier(models.Model):
    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created By"),
        on_delete=models.SET(get_sentinel_user),
        related_name='user_supplier',
        related_query_name='supplier_user'
    )

    company_name = models.CharField(
        _("Company Name"),
        max_length=50,
        unique=True
    )

    address = models.TextField(
        _("Company Address")
    )

    contact_no = models.CharField(
        _("Contact Number"),
        max_length=11,
        validators=[
            RegexValidator(
                '^[0-9]{10,11}$',
                _("Please enter a valid phone number")
            )
        ]
    )

    contact_person = models.CharField(
        _("Contact Person"),
        max_length=254
    )

    slug = models.SlugField(
        _("Supplier Slug"),
        blank=True,
        default=""
    )

    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True
    )

    objects = managers.SupplierManager()

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.company_name)

        super(Supplier, self).save(*args, **kwargs)


class Product(models.Model):
    supplier = models.ForeignKey(
        Supplier,
        verbose_name=_("Product Supplier"),
        on_delete=models.CASCADE,
        related_name='supplier_product',
        related_query_name='product_supplier'
    )

    name = models.CharField(
        _("Product Name"),
        max_length=255
    )

    spec = models.TextField(
        _("Product Specification"),
        blank=True
    )

    slug = models.SlugField(
        _("Product Slug"),
        blank=True,
        default=""
    )

    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created By"),
        on_delete=models.SET(get_sentinel_user),
        related_name='user_product',
        related_query_name='product_user'
    )

    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True
    )

    def total_per_product(self):
        return Stock.objects.total_stock(self)

    objects = managers.ProductManager()

    def get_stock(self):
        return self.o

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.slug == "":
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)


def image_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'protected/{0}/{1}/{2}'.format(
        instance.product.supplier.company_name,
        instance.product.name,
        filename
    )


class ProductImage(models.Model):

    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name='product_productimage',
        related_query_name='productimage_product'
    )

    image_name = models.CharField(
        _("Image Name"),
        max_length=50
    )

    description = models.TextField(
        _("Product Description"),
        max_length=255
    )

    image = models.ImageField(
        _("Product Image"),
        upload_to=image_directory_path,
    )

    created_by = models.ForeignKey(
        User,
        verbose_name=_("Created By"),
        on_delete=models.SET(get_sentinel_user),
        related_name='user_productimage',
        related_query_name='productimage_user'
    )

    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True
    )

    objects = managers.ProductImageManager()

    def __str__(self):
        return f'{self.product.name} image'


class Stock(models.Model):
    product = models.ForeignKey(
        Product,
        verbose_name=_("Product"),
        on_delete=models.CASCADE,
        related_name='stock_product',
        related_query_name='product_stock'
    )

    quantity = models.IntegerField(
        _("Stock Quantity")
    )

    created = models.DateTimeField(
        _("Created at"),
        auto_now_add=True
    )

    def total_stock(self, product):
        return Stock.objects.total_stock_by_product(product)

    objects = managers.StockManager()

    def __str__(self):
        return f'{self.product.name} stock movement at {self.created}'
