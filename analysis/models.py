# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class StockName(models.Model):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-updated']
        verbose_name = "Stock Name"
        verbose_name_plural = "Stock Names"

    def __str__(self):
        return self.name

class StockPrices(models.Model):
    stock_id = models.ForeignKey(StockName, on_delete=models.CASCADE)
    stock_date = models.DateTimeField()
    stock_open = models.DecimalField(max_digits=20, decimal_places=2)
    stock_high = models.DecimalField(max_digits=20, decimal_places=2)
    stock_low = models.DecimalField(max_digits=20, decimal_places=2)
    stock_close = models.DecimalField(max_digits=20, decimal_places=2)
    stock_volume = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-stock_date']
        verbose_name = "Stock Price"
        verbose_name_plural = "Stock Prices"

    def __str__(self):
        return ('{} -- {}').format(str(self.stock_id),str(self.stock_date.strftime('%d, %b %Y')))

    def get_percentage(self):
        """
        The Calculation for getting percantage change in closing prices of
        Current and Previous Data
        """
        last_obj = StockPrices.objects.filter(stock_id=self.stock_id).last()
        percanatage = ((self.stock_close-last_obj.stock_close)/last_obj.stock_close)*100
        return percanatage


    