# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2023. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2023. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         17/01/23 10:39 PM
# Project:      CFHL Transactional Backend
# Module Name:  send_code
# Description:
# ****************************************************************
import string
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.utils.translation import gettext as __
from zibanu.django.utils import Email


class SendCode:
    def __init__(self, to: str, action: str, context: dict = None):
        self.__action = action
        self.__to = to
        self.__context = context
        self.__subject_prefix = _(string.capwords(self.__action.replace("_", " ")))
        self.__email_subject = self.__subject_prefix + " / " + __("Authorization Code")
        self.__email = Email(subject=self.__email_subject, from_email=settings.ZB_MAIL_DEFAULT_FROM, to=[to])

    def load_templates(self, context: dict = None) -> bool:
        b_return = False
        # Override context private property
        if context is not None:
            self.__context = context
        if self.__context is not None:
            template_text = self.__action.lower() + ".txt"
            template_html = self.__action.lower() + ".html"
            self.__email.set_html_template(template_html, context=self.__context)
            self.__email.set_text_template(template_text, context=self.__context)
            b_return = True
        return b_return

    def send(self):
        self.__email.send()


