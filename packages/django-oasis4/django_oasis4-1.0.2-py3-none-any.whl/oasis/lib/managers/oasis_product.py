# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 4:48 PM
# Project:      CFHL Transactional Backend
# Module Name:  product
# Description:
# ****************************************************************
from zibanu.django.db import models


class OasisProduct(models.Manager):
    def get_queryset(self):
        return super().get_queryset().using("oasis")

    def get_products_by_classification(self, classification_id: int) -> models.QuerySet:
        queryset = self.get_queryset().filter(classificationid__exact=classification_id).values("productid", "productname", "state")
        return queryset
