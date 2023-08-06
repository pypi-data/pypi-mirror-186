# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 3:51 PM
# Project:      CFHL Transactional Backend
# Module Name:  __init__.py
# Description:
# ****************************************************************
from .oasis_models import Classification
from .oasis_models import Client
from .oasis_models import Discount
from .oasis_models import GeographicLocation
from .oasis_models import OasisProduct
from .oasis_models import TypeClient
from .local_models import DocumentType
from .local_models import Product

__all__ = [
    "Classification",
    "Client",
    "Discount",
    "DocumentType",
    "GeographicLocation",
    "Product",
    "OasisProduct",
    "TypeClient"
]

