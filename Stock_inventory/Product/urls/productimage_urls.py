from django.urls import path
from Product import views

urlpatterns = [
    path('form/', views.ProductImageFormView, name='product_image_form_view'),
    path('<int:id>/', views.ProductImageDisplay, name='productimage_display')
]
