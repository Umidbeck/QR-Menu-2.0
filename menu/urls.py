from django.urls import path
from . import views

urlpatterns = [
    # Customer-facing views
    path('', views.menu_display, name='menu_display'),
    path('category/<slug:category_slug>/', views.menu_display, name='menu_by_category'),
    
    # Admin panel views
    path('admins/panel/', views.admin_panel, name='admin_panel'),
    path('logout/', views.logout_view, name='logout'),
    path('admins/product/add/', views.ProductCreate.as_view(), name='product_add'),
    path('admins/product/<int:pk>/edit/', views.ProductUpdate.as_view(), name='product_edit'),
    path('admins/product/<int:pk>/delete/', views.ProductDelete.as_view(), name='product_delete'),
    path('admins/product/<int:pk>/toggle/', views.toggle_availability, name='product_toggle'),
]