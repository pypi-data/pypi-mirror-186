# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         18/01/23 3:16 PM
# Project:      CFHL Transactional Backend
# Module Name:  user_profile
# Description:
# ****************************************************************
from django.contrib.auth.models import User
from django.db import transaction
from oasis.models import DocumentType
from zibanu.django.db import models


class UserProfile(models.Manager):
    """
    Override manager class for entity UserProfile
    """
    def create_from_customer_data(self, customer_data: dict):
        try:
            qs = DocumentType.objects.get_record_by_type(customer_data.get("document_type"))
            if qs is not None:
                document_type = qs.get()
                transaction.set_autocommit(False)
                user = User.objects.create_user(customer_data.get("customer_id"),
                                                customer_data.get("email"),
                                                customer_data.get("password"))
                user.first_name = customer_data.get("first_name")
                user.last_name = customer_data.get("last_name")
                user.save()
                # Create profile
                profile = self.model()
                profile.user = user
                profile.document_type = document_type
                profile.document_id = customer_data.get("customer_id")
                profile.location = customer_data.get("location")
                profile.address = customer_data.get("address")
                profile.phone = customer_data.get("phone")
                profile.mobile = customer_data.get("mobile")
                profile.type = customer_data.get("type")
                profile.save(force_insert=True)
        except Exception as exc:
            transaction.rollback()
        else:
            transaction.commit()
        finally:
            transaction.set_autocommit(False)

