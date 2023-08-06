# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 10:29 AM
# Project:      CFHL Transactional Backend
# Module Name:  models
# Description:
# ****************************************************************
from coffee_price.lib import managers
from django.utils.translation import gettext_lazy as _
from oasis.models import Product
from zibanu.django.db import models


class Price(models.Model):
    """
    Model class to represent prices table
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_("Created at"), null=False, blank=False)
    product = models.ForeignKey(Product, blank=False, null=False, verbose_name=_("Product"),
                                on_delete=models.PROTECT, related_name="prices", related_query_name="product")
    date_from = models.DateTimeField(blank=False, null=False, verbose_name=_("From"))
    date_to = models.DateTimeField(blank=False, null=False, verbose_name=_("To"))
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=False, null=False, default=0,
                                verbose_name=_("Product price"))
    # Set default manager
    objects = managers.Price()

    class Meta:
        indexes = [
            models.Index(fields=("product", "date_from", "date_to"))
        ]
