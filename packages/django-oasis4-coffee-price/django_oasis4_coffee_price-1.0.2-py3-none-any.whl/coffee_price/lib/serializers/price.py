# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         13/12/22 7:50 AM
# Project:      CFHL Transactional Backend
# Module Name:  coffee_price
# Description:
# ****************************************************************
import pytz
from coffee_price.models import Price
from django.conf import settings
from django.utils import timezone
from zibanu.django.rest_framework import serializers


class PriceListSerializer(serializers.ModelSerializer):
    """
    Serializer class for Price entity.
    """
    product = serializers.SlugRelatedField(many=False, read_only=True, slug_field="name")
    price = serializers.SerializerMethodField(default=0)
    factor = serializers.SerializerMethodField(default=settings.COFFEE_PRICE_BASE_FACTOR)
    date_from = serializers.SerializerMethodField()
    date_to = serializers.SerializerMethodField()

    class Meta:
        """
        Serializer Meta Class
        """
        model = Price
        fields = ("product", "date_from", "date_to", "price", "factor")

    def get_date_from(self, instance):
        """
        Return a date_from field with default format or get format from context.
        :param instance: model instance
        :return: string with formatted date
        """
        date_format = self.context.get("date_format", "%Y-%m-%d %I:%M %p")
        date_from = instance.date_from.astimezone(timezone.get_default_timezone())
        return date_from.strftime(date_format)

    def get_date_to(self, instance):
        """
        Return a date_to field with default format or get format from context.
        :param instance: model instance
        :return: string with formatted date
        """
        date_format = self.context.get("date_format", "%Y-%m-%d %I:%M %p")
        date_to = instance.date_to.astimezone(timezone.get_default_timezone())
        return date_to.strftime(date_format)

    def get_price(self, instance):
        """
        Methodfield to return price with load
        :param instance: queryset model instance
        :return: calculated price
        """
        factor = self.get_factor(instance)

        if "kg" in self.context:
            price = instance.price
        else:
            price = instance.price * settings.COFFEE_PRICE_KG_BY_LOAD

        price = Price.objects.calc_price(price, factor)

        return price

    def get_factor(self, instance):
        """
        Method field to return base factor to calculate price
        :param instance: queryset model instance
        :return: factor from settings
        """
        factor = self.context.get("factor", settings.COFFEE_PRICE_CALC_FACTOR)
        return factor
