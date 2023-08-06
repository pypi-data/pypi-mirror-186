# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 4:53 PM
# Project:      CFHL Transactional Backend
# Module Name:  own_product
# Description:
# ****************************************************************
from zibanu.django.db import models


class Product(models.Manager):

    def get_by_product(self, product_id: int) -> models.Model:
        """
        Return a product record based on id received by parameters
        :param product_id: product id
        :return: product record
        """
        return self.get_queryset().filter(product_id__exact=product_id).get()

    def get_by_products(self, product_list: list) -> models.QuerySet:
        """
        Return a set of records based on product list received by parameters
        :param product_list: product list
        :return: queryset with set of records
        """
        return self.get_queryset().filter(product_id__in=product_list)

