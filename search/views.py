from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from products.models import Product

class SearchProductResultListView(ListView):
  template_name = 'list.html'

  def get_queryset(self, *args, **kwargs):
    request = self.request
    query = request.GET.get('q')
    if query is not None:
      return Product.objects.filter(title__icontains=query)
    else:
      return Product.objects.all()

class SearchProductListView(ListView):
  template_name = 'list.html'

  def get_queryset(self, *args, **kwargs):
    return Product.objects.all()