# -*- coding: utf-8 -*-
import decimal

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         11/12/22 2:41 PM
# Project:      CFHL Transactional Backend
# Module Name:  coffee_price
# Description:
# ****************************************************************
from coffee_price import models
from coffee_price.lib import serializers
from django.conf import settings
from django.db import DatabaseError
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from oasis.lib import serializers as oasis_serializers
from oasis.models import Product
from rest_framework import status
from rest_framework.response import Response
from zibanu.django.rest_framework.exceptions import APIException
from zibanu.django.rest_framework.viewsets import ViewSet


class CoffeePrice(ViewSet):
    def get_prices_list(self, request) -> Response:
        """
        REST service to get a list of prices based con COFFEE_PRICE_PRODICTS setting
        :param request: request data from HTTP
        :return: response object with data and status
        """
        try:
            # Get a naive datetime
            now = timezone.now()
            queryset = models.Price.objects.get_products_price_by_date(date_to_search=now)
            serializer = serializers.PriceListSerializer(instance=queryset, many=True)
            data = serializer.data
            status_return = status.HTTP_200_OK if len(data) > 0 else status.HTTP_204_NO_CONTENT
        except DatabaseError as exc:
            raise APIException(msg=_("Error fetching prices. Please try again later."),
                               http_status=status.HTTP_424_FAILED_DEPENDENCY)
        except Exception as exc:
            raise APIException(msg=_("Not controlled exception error."), error=str(exc)) from exc
        else:
            return Response(status=status_return, data=data)

    def get_product_list(self, request) -> Response:
        """
        REST service that return a list of products based on "COFFEE_PRICE_PRODUCTS" setting
        :param request: request data from HTTP
        :return: response object with status and data
        """
        try:
            product_list = [int(x) for x in settings.COFFEE_PRICE_PRODUCTS.split(",")]
            queryset = Product.objects.get_by_products(product_list=product_list).order_by("name")
            serializer = oasis_serializers.ProductListSerializer(instance=queryset, many=True)
            data = serializer.data
            status_return = status.HTTP_200_OK if len(data) > 0 else status.HTTP_204_NO_CONTENT
        except DatabaseError as exc:
            raise APIException(msg=_("Error fetching prices. Please try again later."), error=str(exc),
                               http_status=status.HTTP_424_FAILED_DEPENDENCY)
        except Exception as exc:
            raise APIException(msg=_("Not controlled exception error."), error=str(exc)) from exc
        else:
            return Response(status=status_return, data=data)

    def get_product_price(self, request) -> Response:
        """
        REST service that return a price for a specific product
        :param request: request data from HTTP {"product_id", "factor"}. If factor does not exist,
        COFFEE_PRICE_CALC_FACTOR will be taken by default.
        :return: response object with status and data
        """
        try:
            if request.data is not None:
                if "product" in request.data:
                    now = timezone.now()
                    # Get parameters. If "factor" is not send in request, set default value
                    product = request.data.get("product")
                    factor = request.data.get("factor", settings.COFFEE_PRICE_CALC_FACTOR)
                    queryset = models.Price.objects.get_by_product(product_id=product, date_to_search=now)
                    serializer = serializers.PriceListSerializer(instance=queryset, context={"factor": factor},
                                                                 many=True)
                    data = serializer.data
                    if data is not None and len(data) > 0:
                        price_kg = round(decimal.Decimal(data[0]["price"]) / settings.COFFEE_PRICE_KG_BY_LOAD)
                        data[0]["price_kg"] = price_kg
                    status_return = status.HTTP_200_OK if len(data) > 0 else status.HTTP_204_NO_CONTENT
                else:
                    raise APIException(msg=_("Data request not found."), http_status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                raise APIException(msg=_("Data request not found."), http_status=status.HTTP_406_NOT_ACCEPTABLE)
        except DatabaseError as exc:
            raise APIException(msg=_("Error fetching prices. Please try again later."), error=str(exc),
                               http_status=status.HTTP_424_FAILED_DEPENDENCY) from exc
        except ObjectDoesNotExist as exc:
            raise APIException(msg=_("Product does not exists."), error=str(exc), http_status=status.HTTP_404_NOT_FOUND)
        except Exception as exc:
            raise APIException(msg=_("Not controlled exception error."), error=str(exc)) from exc
        else:
            return Response(status=status_return, data=data)
