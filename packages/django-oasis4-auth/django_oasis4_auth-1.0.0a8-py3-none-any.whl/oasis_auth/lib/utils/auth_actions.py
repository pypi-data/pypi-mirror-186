# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         18/01/23 10:12 AM
# Project:      CFHL Transactional Backend
# Module Name:  auth_actions
# Description:
# ****************************************************************
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError
from oasis_auth.models import UserProfile
from typing import Any


class AuthActions:
    """
    Class to encapsulate the different actions to be executed for auth package
    depending on action required.
    """
    def __init__(self, data: dict):
        """
        Initialization method
        :param data: data dictionary with at least "data" and "action" keys.
        """
        if data is not None and {"data", "action"} <= data.keys():
            self.__data = data.get("data")
            self.__action = data.get("action")
            self.__password = data.get("password")
        else:
            raise ValidationError(_("Invalid initialization data class."))

    def __get_method(self):
        return "_" + self.__action

    def do_action(self) -> Any:
        if hasattr(self, self.__get_method()):
            # Get the method of class to invoke
            method = getattr(self, self.__get_method())
            # Invoke method
            return method()
        else:
            raise ValidationError(_("Action does not have associated method."))

    def _pre_register(self) -> bool:
        UserProfile.objects.create_from_customer_data(self.__data)





