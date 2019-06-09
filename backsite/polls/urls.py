# -*- coding: utf-8 -*-
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('data-change/date-change',views.DbChange.date_change),
    path('data-change/goods-change',views.DbChange.goods_change),
    path('data-change/site-change',views.DbChange.site_change),
    path('data-change/change',views.DbChange.change),
    path('data-change/anaylse',views.DbChange.anaylse),
    path('apriori/getdata',views.Apriori.apriori_data,name='apriori'),
    path('apriori/getresult',views.Apriori.apriori_run,name='apriori')
]