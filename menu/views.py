from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from .models import Product, Category
from .forms import ProductForm
from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('menu_display')

def menu_display(request, category_slug=None):
    """View for customers to see the menu"""
    categories = Category.objects.all()
    
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category, available=True)
    else:
        products = Product.objects.filter(available=True)
        category = None
    
    context = {
        'category': category,
        'categories': categories,
        'products': products
    }
    return render(request, 'menu/menu_display.html', context)

@login_required
def admin_panel(request):
    """Admin panel for managing products"""
    categories = Category.objects.all()
    products = Product.objects.all().order_by('category', 'name')
    
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, 'menu/admin_panel.html', context)

class ProductCreate(LoginRequiredMixin, CreateView):
    """View for creating a new product"""
    model = Product
    form_class = ProductForm
    template_name = 'menu/product_form.html'
    success_url = reverse_lazy('admin_panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add New Product'
        return context

class ProductUpdate(LoginRequiredMixin, UpdateView):
    """View for updating an existing product"""
    model = Product
    form_class = ProductForm
    template_name = 'menu/product_form.html'
    success_url = reverse_lazy('admin_panel')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edit Product'
        return context

class ProductDelete(LoginRequiredMixin, DeleteView):
    """View for deleting a product"""
    model = Product
    success_url = reverse_lazy('admin_panel')
    
    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.delete()
        return JsonResponse({'success': True, 'redirect_url': success_url})

@login_required
def toggle_availability(request, pk):
    """Toggle product availability"""
    product = get_object_or_404(Product, pk=pk)
    product.available = not product.available
    product.save()
    return JsonResponse({'status': 'success', 'available': product.available})

