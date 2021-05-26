from django.db.models import Sum
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)
from django.contrib.auth.decorators import login_required
from sendfile import sendfile
from .models import (
    ProductImage,
    Supplier,
    Product,
    Stock,
)

from .forms import (
    SupplierCreateForm,
    SupplierUpdateForm,
    ProductCreateForm,
    ProductUpdateForm,
    ProductImageInlineFormSet,
    StockCreateForm
)
# Create your views here.


def SupplierListView(request):
    try:
        suppliers = Supplier.objects.all()
    except Supplier.DoesNotExist:
        suppliers = None

    context = {
        'suppliers': suppliers
    }

    return render(request, 'Product/Supplier/list_view.html', context)


def SupplierCreateView(request):
    form = SupplierCreateForm(request.POST or None)
    if form.is_valid():
        supplier_create_form = form.save(commit=False)
        supplier_create_form.created_by = request.user
        supplier_create_form.save()
        return redirect('supplier_detail_view', supplier_create_form.slug)

    context = {
        'form': form,
    }

    return render(request, 'Product/Supplier/create_view.html', context)


def SupplierDetailView(request, slug):
    supplier = get_object_or_404(Supplier, slug=slug)

    stock_item = Stock.objects.filter(
        product__supplier=supplier
    ).values(
        'product__slug',
        'product__name',
    ).annotate(
        stock=Sum('quantity')
    )

    context = {
        'supplier': supplier,
        'stock_item': stock_item
    }

    return render(request, 'Product/Supplier/detail_view.html', context)


def SupplierUpdateView(request, slug):
    supplier = get_object_or_404(Supplier, slug=slug)
    form = SupplierUpdateForm(request.POST or None, instance=supplier)
    if form.is_valid():
        supplier_update_form = form.save(commit=False)
        supplier_update_form.save()
        return redirect('supplier_detail_view', slug)

    context = {
        'supplier': supplier,
        'form': form,
    }

    return render(request, 'Product/Supplier/update_view.html', context)


def SupplierDeleteRedirect(request, slug):
    supplier = get_object_or_404(Supplier, slug=slug)
    supplier.delete()
    return redirect('supplier_list_view')


def ProductCreateView(request, slug):
    supplier = get_object_or_404(Supplier, slug=slug)
    form = ProductCreateForm(request.POST or None)
    if form.is_valid():
        product_form = form.save(commit=False)
        product_form.supplier = supplier
        product_form.created_by = request.user
        product_form.save()
        return redirect('product_detail_view', supplier.slug, product_form.slug)

    context = {
        'supplier': supplier,
        'form': form,
    }

    return render(request, "Product/Product/create_view.html", context)


def ProductDetailView(request, slug, product_slug):
    product = get_object_or_404(
        Product,
        supplier__slug=slug,
        slug=product_slug
    )

    current_stock = product.total_per_product()

    context = {
        'product': product,
        'current_stock': current_stock
    }

    return render(request, "Product/Product/detail_view.html", context)


def ProductUpdateView(request, slug, product_slug):
    product = get_object_or_404(
        Product,
        supplier__slug=slug,
        slug=product_slug
    )
    form = ProductUpdateForm(request.POST or None, instance=product)
    if form.is_valid():
        product_form = form.save(commit=False)
        product_form.save()
        return redirect('product_detail_view', product.supplier.slug, product_form.slug)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, "Product/Product/update_view.html", context)


def ProductDeleteRedirect(request, slug, product_slug):
    product = get_object_or_404(
        Product,
        supplier__slug=slug,
        slug=product_slug
    )

    product.delete()

    return redirect('supplier_detail_view', slug)


def ProductImageFormView(request, slug, product_slug):
    product = get_object_or_404(
        Product,
        supplier__slug=slug,
        slug=product_slug
    )

    formset = ProductImageInlineFormSet(
        request.POST or None,
        request.FILES or None,
        instance=product
    )
    if formset.is_valid():
        product_images = formset.save(commit=False)
        for product_image in product_images:
            product_image.created_by = request.user
            product_image.save()
        return redirect('product_detail_view', product.supplier.slug, product.slug)

    context = {
        'product': product,
        'formset': formset,
    }

    return render(request, "Product/Product_Image/form_view.html", context)


def ProductImageDisplay(request, slug, product_slug, id):
    image = get_object_or_404(
        ProductImage,
        product__supplier__slug=slug,
        product__slug=product_slug,
        id=id
    )
    return sendfile(request, image.image.path)


def StockCreateView(request, slug, product_slug):
    product = get_object_or_404(
        Product,
        supplier__slug=slug,
        slug=product_slug
    )

    form = StockCreateForm(
        request.POST or None,
    )

    if form.is_valid():
        stock = form.save(commit=False)
        stock.product = product
        stock.save()
        print(stock)
        return redirect('product_detail_view', product.supplier.slug, product.slug)

    context = {
        'product': product,
        'form': form,
    }

    return render(request, "Product/Stock/create_view.html", context)
