# -*- coding: utf-8 -*-
import os
#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/01/23 1:47 PM
# Project:      CFHL Transactional Backend
# Module Name:  code_generator
# Description:
# ****************************************************************
import os
from uuid import SafeUUID, UUID


class CodeGenerator:
    def __init__(self, action: str, is_safe: SafeUUID = SafeUUID.safe):
        self._action = action
        self._code = None
        self._is_safe = is_safe

    @property
    def is_safe(self):
        return self._is_safe

    @is_safe.setter
    def is_safe(self, value: SafeUUID):
        self._is_safe = value

    @property
    def code(self) -> int:
        return self._code

    @property
    def action(self) -> str:
        return self._action

    @action.setter
    def action(self, value: str = None):
        self._action = value

    def _get_uuid(self, is_safe: SafeUUID = SafeUUID.safe):
        uuid = UUID(bytes=os.urandom(16), version=4, is_safe=is_safe)
        return uuid


    def generate_code(self):
        return self.token, self.code
