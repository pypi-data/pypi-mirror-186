# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         11/12/22 2:36 PM
# Project:      CFHL Transactional Backend
# Module Name:  urls
# Description:
# ****************************************************************
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from coffee_price.lib import services

routers = DefaultRouter()

urlpatterns = [
    path(r"", include(routers.get_urls())),
    path(r"list/", services.CoffeePrice.as_view({"post": "get_prices_list"})),
    path(r"product-list/", services.CoffeePrice.as_view({"post": "get_product_list"})),
    path(r"product-price/", services.CoffeePrice.as_view({"post": "get_product_price"}))
]
