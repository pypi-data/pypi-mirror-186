# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         20/12/22 6:10 AM
# Project:      CFHL Transactional Backend
# Module Name:  client
# Description:
# ****************************************************************
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _
from oasis.lib.choices import CustomerType
from typing import Any
from zibanu.django.db import models


class Client(models.Manager):
    """
    Default manager for Client model
    """

    def get_by_pk(self, pk: Any, customer_status: str = None) -> models.QuerySet:
        """
        Override a default class method
        :param pk: customer id for query
        :param customer_status: state of customer to validate
        :return: queryset with data
        """
        qs = self.get_queryset().filter(clientid__exact=pk)
        if customer_status is not None:
            qs = qs.filter(state__exact=customer_status)
        if len(qs) == 0:
            raise self.model.DoesNotExist(_("OASIS Error. The customer does not exists."))
        return qs

    def get_customer(self, customer_id: int, email: str) -> models.Model:
        """
        Get a Customer object with validations if email and document id are valid
        :param customer_id: customer id for search
        :param email: email to validate
        :return:
        """
        # Change email and set standard
        email = email.strip().lower()
        # Get customer from OASIS table
        qs = self.get_by_pk(pk=customer_id, customer_status="A")
        customer = qs.first()
        if ";" in customer.email:
            customer_email = customer.email.split(";")[0].strip().lower()
            customer.email = customer_email
        else:
            customer_email = customer.email.strip().lower()

        # Validate customer and set customer type.
        try:
            validate_email(customer_email)
            customer.is_valid = True if email == customer_email else False
            if customer.partner == 1:
                customer.customer_type = CustomerType.PARTNER
            elif customer.customer == 1 or customer.supplier == 1:
                customer.customer_type = CustomerType.CUSTOMER
            else:
                raise ValidationError(_("The customer does not belong to the company."))
        except ValidationError as exc:
            customer.is_valid = False
            raise ValidationError(exc) from exc

        return customer

