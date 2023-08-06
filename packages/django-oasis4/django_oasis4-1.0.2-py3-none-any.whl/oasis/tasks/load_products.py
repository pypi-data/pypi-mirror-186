# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 4:02 PM
# Project:      CFHL Transactional Backend
# Module Name:  load_products
# Description:
# ****************************************************************
from core import celery_app
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from oasis import models
from typing import Any


@celery_app.task(bind=True)
def load_products(app: Any):
    """
    Shared task for load a list of products from OASIS database
    :return: None
    """
    classification_id = settings.OASIS_COFFEE_PRODUCT_CLASSIFICATION_ID
    products = models.OasisProduct.objects.get_products_by_classification(classification_id)

    if products is not None and len(products) > 0:
        for product in products:
            own_product = models.Product()
            product_name = product.get("producname1") if product.get("producname1") is not None else product.get(
                "productname")
            try:
                own_product = models.Product.objects.get_by_product(product_id=product.get("productid"))
                own_product.name = product_name
                own_product.product_id = product.get("productid")
                own_product.is_enabled = True if product.get("state") == "A" else False
            except ObjectDoesNotExist:
                own_product = models.Product(name=product_name, product_id=product.get("productid"))
            except Exception as exc:
                print(exc)
            finally:
                own_product.save()
