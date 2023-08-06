# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 3:52 PM
# Project:      CFHL Transactional Backend
# Module Name:  __init__.py
# Description:
# ****************************************************************
from oasis.tasks.load_products import load_products

__all__ = [
    "load_products"
]
