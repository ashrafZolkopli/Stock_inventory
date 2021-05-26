from django.urls import path, include
from Product import views

urlpatterns = [
    path('', views.SupplierListView, name='supplier_list_view'),
    path(
        'create/',
        views.SupplierCreateView,
        name='supplier_create_view'
    ),
    path(
        '<slug:slug>/',
        include([
            path(
                '',
                views.SupplierDetailView,
                name='supplier_detail_view'
            ),
            path(
                'update/',
                views.SupplierUpdateView,
                name='supplier_update_view'
            ),
            path(
                'delete/',
                views.SupplierDeleteRedirect,
                name='supplier_delete_redirect'
            ),
            path('', include('Product.urls.product_urls')),
        ])
    )
]
