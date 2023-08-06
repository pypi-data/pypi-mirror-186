# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         17/01/23 5:07 PM
# Project:      CFHL Transactional Backend
# Module Name:  document_type
# Description:
# ****************************************************************
from zibanu.django.db import models


class DocumentType(models.Manager):

    def get_record_by_type(self, type_id: str = None) -> models.QuerySet:
        return self.get_queryset().filter(type_id__exact=type_id)

    def save_or_create(self, type_id: str = None, description: str = None) -> bool:
        try:
            qs = self.get_record_by_type(type_id=type_id)
            if qs.count() == 0:
                document_type = self.model()
                document_type.type_id = type_id
                document_type.description = description
            else:
                document_type = qs.get()
                document_type.description = description
            document_type.save()
        except Exception:
            b_return = False
        else:
            b_return = True
        finally:
            return b_return



