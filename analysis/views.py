# Prividing Stock Related Views
from __future__ import unicode_literals

#builtin django imports
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView

#Custom Model Data
from analysis.models import StockName, StockPrices

#Pagination
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#To list all Stock Names
class StockListView(ListView):
    """
    This class is using for listing out
    the Stock Names from StockName Model

    """
    model = StockName
    context_object_name = "stocks"
    template_name = "index.html"

    # queryset will return the value list of Stock Names
    def get_queryset(self, **kwargs):
        stocks = StockName.objects.filter() \
                           .values_list('id', 'name')
        return stocks #stock with name and id returns


#To list individual Company Share's
class StockDetailView(DetailView):
    """
    The Class for Detail View from the listing Stocks
    Which will provide the Paginated StockPrices and Stock objects details
    """
    model = StockName
    template_name = "stock_details.html"

    def get_context_data(self, **kwargs):
        """
        Context will return the paginated StockPrices
        And the last 5 stock volumes

        """
        context = super(StockDetailView, self).get_context_data(**kwargs)
        try:
            #the Stock Price details of Stock ID, which will taken as slug.
            # note: slug,pk = self.kwargs.get('pk')
            stock_detail_obj = StockPrices.objects.select_related().filter(stock_id=self.kwargs.get('pk'))
            paginator = Paginator(stock_detail_obj, 10) # Show 10 contacts per page

            page = self.request.GET.get('page')
            try:
                stock_data = paginator.page(page)
            except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                stock_data = paginator.page(1)
            except EmptyPage:
                # If page is out of range (e.g. 9999), deliver last page of results.
                stock_data = paginator.page(paginator.num_pages)
        except StockPrices.DoesNotExist:
            stock_detail_obj = None

        # List volume of each share
        try:
            volume_dict_list = stock_detail_obj.values_list("stock_volume", "stock_date")
        except Exception as e:
            volume_dict_list = None
        bool(stock_data) # queryset is evaluated  and results are cached
        bool(volume_dict_list) # queryset is evaluated  and results are cached
        context['stock_data'] = stock_data #  uses the cache
        context['volume_dict_list'] = volume_dict_list[:5]#  uses the cache
        return context

