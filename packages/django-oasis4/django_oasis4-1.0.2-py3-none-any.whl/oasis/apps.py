# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         16/11/22 9:12 AM
# Project:      CFHL Transactional Backend
# Module Name:  apps
# Description:
# ****************************************************************
from django.conf import settings
from django.apps import AppConfig


class OasisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'oasis'

    def ready(self):
        """
        Event that is fired when the module loads correctly.
        :return:
        """
        settings.OASIS_COFFEE_BASE_PRODUCT = getattr(settings, "OASIS_COFFEE_BASE_PRODUCT", 0)
        settings.OASIS_COFFEE_BASE_DISCOUNT = getattr(settings, "OASIS_COFFEE_BASE_DISCOUNT", 2)
        settings.OASIS_DEFAULT_LOCATION = getattr(settings, "OASIS_DEFAULT_LOCATION", 0)
        settings.OASIS_COFFEE_PRODUCT_CLASSIFICATION_ID = getattr(settings, "OASIS_COFFEE_PRODUCT_CLASSIFICATION_ID", 1111)

