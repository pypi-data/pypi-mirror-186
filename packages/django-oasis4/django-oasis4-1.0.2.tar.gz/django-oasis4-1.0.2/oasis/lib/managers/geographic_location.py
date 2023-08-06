# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         17/01/23 6:22 AM
# Project:      CFHL Transactional Backend
# Module Name:  geographic_location
# Description:
# ****************************************************************
from django.utils.translation import gettext_lazy as _
from typing import Any
from zibanu.django.db import models


class GeographicLocation(models.Manager):
    """
    GeographicLocation entity manager
    """
    def get_by_pk(self, pk: Any) -> models.QuerySet:
        """
        Method override for get_by_pk default method
        :param pk: fake pk for get location from it´s id
        :return: queryset if found, else raise DoesNotExists exception
        """
        qs = self.get_queryset().filter(geographiclocationid__exact=pk)
        if len(qs) == 0:
            self.model.DoesNotExist(_("The location does not exists."))
        return qs

