# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import OriOrderdetail,OriClient,OriOrders,OriRegion,OriType,OriCommodity,ChangeFact,ChangeSite,ChangeGoods,ChangeDates
admin.site.register([OriOrderdetail,OriClient,OriOrders,OriRegion,OriType,OriCommodity,ChangeFact,ChangeSite,ChangeGoods,ChangeDates])
# Register your models here.
