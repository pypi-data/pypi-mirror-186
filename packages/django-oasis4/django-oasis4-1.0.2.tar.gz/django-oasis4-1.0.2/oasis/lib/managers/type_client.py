# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         17/01/23 4:53 PM
# Project:      CFHL Transactional Backend
# Module Name:  type_client
# Description:
# ****************************************************************
from zibanu.django.db import models


class TypeClient(models.Manager):
    def get_for_sync(self):
        qs = self.get_queryset().values("typeclientid", "typeclientname").all()
        return qs
