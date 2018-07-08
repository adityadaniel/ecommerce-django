from django.urls import path, include

from .views import SearchProductListView, SearchProductResultListView

urlpatterns = [
    path('', SearchProductResultListView.as_view(), name='search_list'),
]
