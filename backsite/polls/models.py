# coding:utf8
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class ChangeDates(models.Model):
    year = models.PositiveIntegerField()
    month = models.CharField(max_length=12)
    day = models.CharField(max_length=12)

    class Meta:
        managed = False
        db_table = 'change_dates'


class ChangeFact(models.Model):
    datesid = models.PositiveIntegerField(db_column='datesId')  # Field name made lowercase.
    areaid = models.PositiveIntegerField(db_column='areaId')  # Field name made lowercase.
    goodsid = models.PositiveIntegerField(db_column='goodsId')  # Field name made lowercase.
    customerid = models.PositiveIntegerField(db_column='customerId')  # Field name made lowercase.
    total = models.FloatField()
    price = models.FloatField()
    amount = models.PositiveIntegerField()

    class Meta:
        managed = False
        db_table = 'change_fact'


class ChangeGoods(models.Model):
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    kind = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'change_goods'


class ChangeSite(models.Model):
    province = models.CharField(max_length=20)
    city = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'change_site'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class OriClient(models.Model):
    clientname = models.CharField(db_column='clientName', max_length=254, blank=True, null=True)  # Field name made lowercase.
    regionid = models.IntegerField(db_column='regionId', blank=True, null=True)  # Field name made lowercase.
    regionsite = models.CharField(db_column='regionSite', max_length=254, blank=True, null=True)  # Field name made lowercase.
    regionphone = models.CharField(db_column='regionPhone', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_client'


class OriCommodity(models.Model):
    commodityname = models.CharField(db_column='commodityName', max_length=254, blank=True, null=True)  # Field name made lowercase.
    commoditytype = models.CharField(db_column='commodityType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    typeid = models.IntegerField(db_column='typeId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_commodity'


class OriOrderdetail(models.Model):
    orderid = models.IntegerField(db_column='orderID', blank=True, null=True)  # Field name made lowercase.
    commodityid = models.CharField(db_column='commodityID', max_length=254, blank=True, null=True)  # Field name made lowercase.
    detailprice = models.CharField(db_column='detailPrice', max_length=254, blank=True, null=True)  # Field name made lowercase.
    detailaccout = models.IntegerField(db_column='detailAccout', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_orderdetail'


class OriOrders(models.Model):
    bookdate = models.DateField(db_column='bookDate')  # Field name made lowercase.
    deadline = models.DateField()
    total = models.FloatField()
    customerid = models.PositiveIntegerField(db_column='customerId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_orders'


class OriRegion(models.Model):
    regionname = models.CharField(db_column='regionName', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_region'


class OriType(models.Model):
    typename = models.CharField(db_column='typeName', max_length=254, blank=True, null=True)  # Field name made lowercase.
    typestate = models.CharField(db_column='typeState', max_length=254, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ori_type'
