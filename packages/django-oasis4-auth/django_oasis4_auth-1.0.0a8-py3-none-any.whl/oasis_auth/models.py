# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         7/01/23 4:03 PM
# Project:      CFHL Transactional Backend
# Module Name:  models
# Description:
# ****************************************************************
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.utils.translation import gettext_lazy as _
from oasis.lib.choices import CustomerType
from oasis.models import DocumentType
from oasis_auth.lib import managers
from zibanu.django.db import models


class UserProfile(models.Model):
    """
    Entity class for extend user profile definition combined with oasis module
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile", related_query_name="user")
    document_type = models.ForeignKey(DocumentType, on_delete=models.PROTECT, blank=False, null=False,
                                      related_name="profile", related_query_name="document_types")
    document_id = models.BigIntegerField(blank=False, null=False, validators=[
        MinValueValidator(limit_value=1, message=_("The document id is invalid."))])
    location = models.CharField(max_length=150, blank=True, null=False)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=30, blank=True, null=True)
    mobile = models.CharField(max_length=30, blank=True, null=True)
    type = models.IntegerField(choices=CustomerType.choices, default=CustomerType.ANYTHING, blank=False, null=False)
    enabled = models.BooleanField(default=True, blank=False, null=False)
    # Default Manager
    objects = managers.UserProfile()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=("document_type", "document_id"), name="UNQ_UserProfile_Document")
        ]
