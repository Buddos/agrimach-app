from django.urls import path, include
from rest_framework.routers import DefaultRouter   # 👈 this import was missing
from . import views

# API Router
router = DefaultRouter()
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    # Frontend (HTML)
    path('', views.product_list, name='catalog_list'),
    path('<int:pk>/', views.product_detail, name='product_detail'),

    # API
    path('api/', include(router.urls)),
]
