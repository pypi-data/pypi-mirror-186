# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         11/12/22 2:56 PM
# Project:      CFHL Transactional Backend
# Module Name:  get_prices
# Description:
# ****************************************************************
from coffee_price.models import Price
from core import celery_app
from django.conf import settings
from django.db import DatabaseError
from oasis.models import Discount
from oasis.models import Product
from typing import Any


@celery_app.task(bind=True)
def task_get_prices(app: Any):
    """
    Task to get prices every minute and save local data to query and serv REST way.
    :return: None
    """
    try:
        product_list = [int(x) for x in settings.COFFEE_PRICE_PRODUCTS.split(",")]
        discount_list = [int(x) for x in settings.COFFEE_PRICE_DISCOUNTS.split(",")]

        for product_item in product_list:
            # Get prices from product list
            brought_prices = Discount.objects.get_price(product_code=product_item, discount_list=discount_list)
            if brought_prices is not None and product_item != 0:
                brought_prices["product"] = Product.objects.get_queryset().filter(
                    product_id__exact=product_item).first()
                price_queryset = Price.objects.get_price_by_product_date(product_id=brought_prices.get("product").id,
                                                                         date_from=brought_prices.get("date_from"),
                                                                         date_to=brought_prices.get("date_to"))
                if price_queryset is not None:
                    # If price does not exist, create price record
                    if len(price_queryset) == 0:
                        if brought_prices.get("date_from") is not None:
                            Price.objects.create(product=brought_prices.get("product"),
                                                 date_from=brought_prices.get("date_from"),
                                                 date_to=brought_prices.get("date_to"),
                                                 price=brought_prices.get("price"))
    except DatabaseError as exc:
        raise DatabaseError from exc
    except Exception as exc:
        raise Exception from exc
