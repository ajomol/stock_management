"""stocks URL Configuration

The main URLs included, analysis module
"""
from django.conf.urls import url
from django.contrib import admin
from analysis.views import StockListView, StockDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', StockListView.as_view(), name='stock_list'),
    url(r'^stock/(?P<pk>[-\w]+)/$', StockDetailView.as_view(), name='stock_details'),
]
