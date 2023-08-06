# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         20/12/22 6:35 AM
# Project:      CFHL Transactional Backend
# Module Name:  customer_type
# Description:
# ****************************************************************
from django.utils.translation import gettext_lazy as _
from zibanu.django.db import models


class CustomerType(models.IntegerChoices):
    """
    Customer types to work
    """
    ANYTHING = 0, _("Not bound")
    CUSTOMER = 1, _("Customer")
    PARTNER = 2, _("Partner")