# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Client(models.Model):
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.
    clientname = models.CharField(db_column='clientName', max_length=254, blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionId', blank=True, null=True)  # Field name made lowercase.
    regionsite = models.CharField(db_column='regionSite', max_length=254, blank=True, null=True)  # Field name made lowercase.
    regionphone = models.CharField(db_column='regionPhone', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'client'


class Commodity(models.Model):
    commodityid = models.IntegerField(db_column='commodityID', blank=True, null=True)  # Field name made lowercase.
    commodityna = models.CharField(db_column='commodityNa', max_length=254, blank=True, null=True)  # Field name made lowercase.
    commodityty = models.IntegerField(db_column='commodityTy', blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'commodity'


class Order(models.Model):
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True)  # Field name made lowercase.
    orderdate = models.CharField(db_column='orderDate', max_length=254, blank=True, null=True)  # Field name made lowercase.
    ordergetdat = models.CharField(db_column='orderGetDat', max_length=254, blank=True, null=True)  # Field name made lowercase.
    ordermoney = models.CharField(db_column='orderMoney', max_length=254, blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='clientID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'


class Orderdetail(models.Model):
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True)  # Field name made lowercase.
    detailid = models.IntegerField(db_column='detailID', blank=True, null=True)  # Field name made lowercase.
    commodityid = models.CharField(db_column='commodityID', max_length=254, blank=True, null=True)  # Field name made lowercase.
    detailprice = models.CharField(db_column='detailPrice', max_length=254, blank=True, null=True)  # Field name made lowercase.
    detailaccou = models.IntegerField(db_column='detailAccou', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'orderdetail'


class Region(models.Model):
    regionid = models.IntegerField(db_column='regionID', blank=True, null=True)  # Field name made lowercase.
    regionname = models.CharField(db_column='regionName', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'region'


class Type(models.Model):
    typeid = models.IntegerField(db_column='typeID', blank=True, null=True)  # Field name made lowercase.
    typename = models.CharField(db_column='typeName', max_length=254, blank=True, null=True)  # Field name made lowercase.
    typestate = models.CharField(db_column='typeState', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'type'
