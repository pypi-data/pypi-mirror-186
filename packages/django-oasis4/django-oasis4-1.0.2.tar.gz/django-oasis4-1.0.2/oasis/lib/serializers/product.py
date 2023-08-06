# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         14/12/22 2:55 PM
# Project:      CFHL Transactional Backend
# Module Name:  product
# Description:
# ****************************************************************
from oasis import models
from zibanu.django.rest_framework import serializers


class ProductListSerializer(serializers.ModelSerializer):
    """
    Serializer class for list of products for frontend choices.
    """

    class Meta:
        model = models.Product
        fields = ("id", "name")

