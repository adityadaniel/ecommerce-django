from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Product

# Create your views here.
class ProductFeaturedListView(ListView):
  queryset = Product.featured_products.all() 
  template_name = 'products/featured/list.html'

class ProductFeaturedDetailView(DetailView):
  queryset = Product.objects.all() 
  template_name = 'products/featured/detail.html'

class ProductListView(ListView):
  queryset = Product.objects.all()
  template_name = 'products/list.html'

class ProductDetailView(DetailView):
  queryset = Product.objects.all()
  template_name = 'products/detail.html'