# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         16/11/22 2:39 PM
# Project:      CFHL Transactional Backend
# Module Name:  discount
# Description:
# ****************************************************************
from django.conf import settings
from django.utils import timezone
from datetime import datetime
from zibanu.django.utils import change_timezone
from zibanu.django.db import models


class Discount(models.Manager):
    """
    Custom manager for entity Discount
    """

    def get_price(self, product_code: int, discount_list: list = []) -> dict:
        """
        Method to obtain a dictionary with price and valid range keys.
        :param product_code: code of product to obtain price
        :param discount_list: list of discounts to add if exists
        :return:
        """
        price_dict = {
            "date_from": None,
            "date_to": None,
            "price": 0
        }
        base_product = settings.OASIS_COFFEE_BASE_PRODUCT
        base_discount = settings.OASIS_COFFEE_BASE_DISCOUNT

        if product_code is not None:
            # Get Base Price
            discount = self.get_product_discounts(product_code=base_product, discount=base_discount)
            if discount is not None:
                price_dict["price"] = discount.price
                price_dict["date_from"] = change_timezone(discount.dateinitial)
                price_dict["date_to"] = change_timezone(discount.datefinal)
                # If Product is different from base
                if product_code != base_product:
                    discount = self.get_product_discounts(product_code=product_code, discount=base_discount)
                    # If product has own base price
                    if discount is not None:
                        price_dict["price"] = discount.price

                    for discount_item in discount_list:
                        # Get another discounts if exists.
                        discount = self.get_product_discounts(product_code=product_code, discount=discount_item)
                        if discount is not None:
                            price_dict["price"] += discount.price

        # Round a price to 0 decimals before ret
        price_dict["price"] = round(price_dict["price"])
        return price_dict

    def get_product_discounts(self, product_code: int = 0, discount: int = 0) -> models.Model:
        """
        Method to get discount price for a product.
        :param product_code: product id, default = 0
        :param discount: discount id, default = 0
        :return:
        """
        # Get default Location
        location = settings.OASIS_DEFAULT_LOCATION
        try:
            # Get a naive datetime
            now = datetime.now()
            # Create a queryset with filter options
            queryset = self.get_queryset().filter(productid__exact=product_code, typediscountid__exact=discount,
                                                  locationid__exact=location)
            # Exclude nulls
            queryset = queryset.exclude(dateinitial=None)
            # Add datetime option to queryset
            queryset = queryset.filter(
                dateinitial__lte=datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute,
                                          tzinfo=timezone.utc),
                datefinal__gte=datetime(year=now.year, month=now.month, day=now.day, hour=now.hour, minute=now.minute,
                                        tzinfo=timezone.utc)).order_by("-dateinitial")
            base_price = queryset.first()
        except Exception as exc:
            raise Exception from exc
        else:
            return base_price
