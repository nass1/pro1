from django.conf.urls import url
from django.contrib import admin
from . import views


app_name = 'chinavAPI'
urlpatterns = [
    url(r'^$',views.mainINDEX,name="mainIndex"),
    url(r'^getprod/$',views.getProducts,name="getprod"),
    url(r'^postprod/$',views.PostToShpify,name="postToShopify"),
    url(r'^getlist/$',views.getList,name="getlist"),
    url(r'^name/$',views.editProduct,name="name"),

]