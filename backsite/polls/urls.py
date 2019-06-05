from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apriori/getdata',views.apriori,name='apriori')
]