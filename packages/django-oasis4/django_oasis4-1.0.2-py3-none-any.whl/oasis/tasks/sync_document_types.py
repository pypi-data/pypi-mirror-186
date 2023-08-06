# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         17/01/23 4:48 PM
# Project:      CFHL Transactional Backend
# Module Name:  sync_document_types
# Description:
# ****************************************************************
from core import celery_app
from oasis import models
from typing import Any


@celery_app.task(bind=True)
def sync_document_types(app: Any):
    try:
        qs = models.TypeClient.objects.get_for_sync()
        if qs:
            for type_client in qs:
                models.DocumentType.objects.save_or_create(type_id=type_client.get("typeclientid"),
                                                           description=type_client.get("typeclientname"))
    except Exception as exc:
        pass
