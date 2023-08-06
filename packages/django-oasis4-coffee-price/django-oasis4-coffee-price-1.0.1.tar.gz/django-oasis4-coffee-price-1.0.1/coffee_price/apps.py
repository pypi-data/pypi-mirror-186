#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado
from django.conf import settings
from django.apps import AppConfig


class CoffeePriceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'coffee_price'

    def ready(self):
        settings.COFFEE_PRICE_BASE_FACTOR = getattr(settings, "COFFEE_PRICE_BASE_FACTOR", 94)
        settings.COFFEE_PRICE_CALC_FACTOR = getattr(settings, "COFFEE_PRICE_CALC_FACTOR", 94)
        settings.COFFEE_PRICE_KG_BY_LOAD = getattr(settings, "COFFEE_PRICE_KG_BY_LOAD", 125)
        settings.COFFEE_PRICE_DISCOUNTS = getattr(settings, "COFFEE_PRICE_DISCOUNTS", "5,6")
        settings.COFFEE_PRICE_PRODUCTS = getattr(settings, "COFFEE_PRICE_PRODUCTS",
                                                 "2101,2102,2104,2106,2107,2109,2112,2113,2114,2126,2120,2134")
