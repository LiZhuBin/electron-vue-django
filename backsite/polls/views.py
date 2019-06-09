# -*- coding: utf-8 -*-

# Create your views here.
import random

from apyori import apriori
from distributed.protocol.serialize import serializers

from django.http import HttpResponse
from . import models
import json


# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")
def index(request):  # 获取数据库的数据
    data = [i.bookdate for i in models.OriOrders.objects.all()]
    return HttpResponse(data)


class DbChange(object):
    dates = models.OriOrders.objects.all()
    commodities = models.OriCommodity.objects.all()
    regions = models.OriRegion.objects.all()
    orders = models.OriOrders.objects.all()
    order_detail = models.OriOrderdetail.objects.all()
    ch_clients = models.OriClient.objects.all()
    ch_date = models.ChangeDates.objects.all()
    ch_site = models.ChangeSite.objects.all()

    @classmethod
    def date_change(cls, request):
        """将数据库数据修改、清洗后存入change_date数据仓库中"""
        objects = []
        for date in cls.dates:
            object = models.ChangeDates(year=str(date.bookdate).split("-")[0], month=str(date.bookdate).split("-")[1],
                                        day=str(date.bookdate), id=date.id)
            object.save()
            objects.append(object)

        return HttpResponse("ff")

    @classmethod
    def goods_change(cls, request):
        """将数据库数据修改、清洗后存入change_goods数据仓库中"""
        object = None
        for commodity in cls.commodities:
            type = models.OriType.objects.get(id=commodity.typeid).typename
            if type:
                object = models.ChangeGoods(id=commodity.id, name=commodity.commodityname,
                                            model=commodity.commoditytype, kind=type)
                object.save()
        return HttpResponse(object)

    @classmethod
    def site_change(cls, request):
        """将数据库数据修改、清洗后存入change_date数据仓库中"""
        object = None
        for region in cls.regions:
            s = region.regionname
            object = models.ChangeSite(id=region.id, province=s[:6], city=s[6:])
            object.save()
        return HttpResponse(object)

    @classmethod
    def change(cls, request):
        object = None
        for order in cls.orders:
            price = float(cls.order_detail.filter(orderid=order.id)[0].detailprice)
            amount = len(cls.order_detail.filter(orderid=order.id)),
            areaid = cls.ch_clients.get(id=order.customerid).regionid,
            goodsid = cls.order_detail.filter(orderid=order.id)[0].commodityid,
            customerid = order.customerid

            object = models.ChangeFact(id=order.id,
                                       datesid=order.id,
                                       areaid=areaid[0],
                                       goodsid=int(goodsid[0]),
                                       customerid=customerid,
                                       price=price,
                                       amount=amount[0],
                                       total=price * amount[0]
                                       )
            a = (order.id, order.id, areaid[0], int(goodsid[0]), price, amount[0], price * amount[0])
            print(a)
            object.save()
        return HttpResponse(a)

    @classmethod
    def getRandom(cls):
        return random.randint(200,1000)

    @classmethod
    def anaylse(cls, request):

        request.encoding = 'utf-8'
        # select_data = request.GET.get('selectData')
        # print("fff"+select_data)
        select_data = {"citiesSelect": ["广州市", "深圳市", "佛山市", "东莞市"],
                       "dataSelect": ["2016-08-05T16:00:00.000Z", "2018-08-13T16:00:00.000Z"],
                       "goodsSelect": ["面包", "奶类", "零食", "酒类"]}
        years = [date.split('-')[0] for date in select_data['dataSelect']]
        months = [date.split('-')[1] for date in select_data['dataSelect']]
        # 得到ch_change中符合year和month的项的id
        # date_id = [i.id for num, year in enumerate(years)for i in cls.ch_date.filter(year=year,month=months[num])]
        # print(select_data)
        # #得到ch_site中符合city等于所选项的id
        # site_id = [city.id for select_city in select_data['citiesSelect']
        #            for city in cls.ch_site.filter(city=u"中山市")]
        #
        # print([year + month for year in years for month in months])
        cities =  ['广州市', '深圳市', '佛山市', '东莞市']
        goods = ['面包', '奶类', '零食']
        dates = ['2019-01','2019-02','2019-03','2019-04']
        b = [{"city":city,"good":good,"date":date,"data":cls.getRandom()}for city in cities for good in goods for date in dates]
        a = [{"label":city,
              "children":[
                  {"lable":good,
                        "children":[
                            {"lable":date,
                                "children":[
                                    {"label":cls.getRandom()}]}]}]} for city in cities for good in goods for date in dates]
        c = [{city:[{good:[{date:cls.getRandom()}]}]}  for city in cities for good in goods for date in dates]
        return HttpResponse(json.dumps(c), content_type="application/json")


class Apriori(object):
    """Apriori module，用于实现apriori算法的实现"""
    url = './data/1000.txt'

    @classmethod
    def __init__(cls, url='./data/1000.txt') -> None:
        """url修改基础数据路径"""
        super().__init__()
        cls.url = url

    @classmethod
    def origin_data(cls):
        with open(cls.url, 'r') as f:
            return [i[2:] for i in f.read().splitlines()]

    @classmethod
    def apriori_data(cls, request):
        """获得用于apriori算法实现的数据（1000条数据）"""
        x = [{'index': str(index), 'item': str(item)} for index, item in enumerate(cls.origin_data())]
        return HttpResponse(json.dumps(x), content_type="application/json")

    @classmethod
    def apriori_run(cls, request):
        """进行apriori运算，返回支持度等结果"""

        def analyse(data):
            result = list(apriori(transactions=data))
            result_change = [{'item-base': str(re.ordered_statistics[0].items_base),
                              'item-add': str(re.ordered_statistics[0].items_add),
                              'support': str(re.support),
                              'confidence': str(re.ordered_statistics[0].confidence)
                              } for re in result]
            return result_change

        return HttpResponse(json.dumps(analyse(cls.origin_data())), content_type="application/json")
