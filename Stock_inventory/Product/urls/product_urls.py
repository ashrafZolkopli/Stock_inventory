from django.urls import path, include
from Product import views

urlpatterns = [
    path('create', views.ProductCreateView, name='product_create_view'),
    path('<slug:product_slug>/', include([
        path('', views.ProductDetailView, name='product_detail_view'),
        path('update/', views.ProductUpdateView, name='product_update_view'),
        path('delete/', views.ProductDeleteRedirect,
             name='product_delete_redirect'),
        path('image/', include('Product.urls.productimage_urls')),
        path('stock/', include('Product.urls.stock_urls'))
    ]))
]
