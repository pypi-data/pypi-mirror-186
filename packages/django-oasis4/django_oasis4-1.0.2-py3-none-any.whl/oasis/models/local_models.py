# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 3:52 PM
# Project:      CFHL Transactional Backend
# Module Name:  own_models
# Description:
# ****************************************************************
from django.utils.translation import gettext_lazy as _
from oasis.lib import managers
from zibanu.django.db import models


class Product(models.Model):
    product_id = models.IntegerField(blank=False, null=False, verbose_name=_("Product id"))
    name = models.CharField(max_length=250, blank=False, null=False, verbose_name=_("Product name"))
    enabled = models.BooleanField(default=True, blank=False, null=False, verbose_name=_("Is enabled"))
    # Set default manager
    objects = managers.Product()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("product_id",), name="ownproduct_productid_unique",)
        ]


class DocumentType(models.Model):
    type_id = models.CharField(max_length=1, blank=False, null=False, verbose_name=_("Document type oasis id"))
    description = models.CharField(max_length=50, blank=False, null=False, verbose_name=_("Document type description"))
    # Set default manager
    objects = managers.DocumentType()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("type_id",), name="UNQ_document_type_id")
        ]
