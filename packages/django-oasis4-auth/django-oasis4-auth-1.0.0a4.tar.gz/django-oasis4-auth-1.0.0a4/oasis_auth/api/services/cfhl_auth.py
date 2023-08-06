# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         20/12/22 12:13 PM
# Project:      CFHL Transactional Backend
# Module Name:  oasis_auth
# Description:
# ****************************************************************
from django.conf import settings
from django.core.cache import cache
from django.core.exceptions import ValidationError as CoreValidationError
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from oasis.models import Client
from oasis.models import GeographicLocation
from rest_framework import status
from rest_framework.response import Response
from uuid import uuid4
from zibanu.django.db.models import ObjectDoesNotExist
from zibanu.django.rest_framework.exceptions import APIException
from zibanu.django.rest_framework.exceptions import ValidationError
from zibanu.django.rest_framework.viewsets import ViewSet
from zibanu.django.utils import numeric_code_generator
from zibanu.django.utils import Email

from oasis.tasks.sync_document_types import sync_document_types


class CfhlAuth(ViewSet):
    """
    Set of POST endpoints for REST services.
    """

    def pre_register(self, request) -> Response:
        """
        REST service to get data and send code for register process.
        :param request:
        :return:
        """
        try:
            if {"customer_id", "email"} <= request.data.keys():
                customer = Client.objects.get_customer(request.data.get("customer_id"), request.data.get("email"))
                if customer.is_valid:
                    cache_key = uuid4().hex
                    generated_code = numeric_code_generator(6)
                    customer_data = {
                        "first_name": customer.first_name,
                        "last_name": customer.last_name,
                        "location": customer.location,
                        "address": customer.address,
                        "phone": customer.phone,
                        "mobile": customer.celphone,
                        "email": customer.email,
                        "customer_id": customer.clientid,
                        "is_valid": customer.is_valid,
                        "type": customer.customer_type,
                    }
                    data_return = {
                        "token": cache_key,
                        "data": customer_data
                    }
                    data_cache = {
                        "code": generated_code,
                        "data": customer_data
                    }
                    email_context = {
                        "customer_name": customer.clientname,
                        "customer_code": generated_code,
                        "code_timeout": settings.CFHL_AUTH_CODE_TIMEOUT,
                        "email_datetime": timezone.now().astimezone(tz=timezone.get_default_timezone()).strftime(
                            "%Y-%m-%d %H:%M:%S"),
                        "email_id": uuid4()
                    }
                    # Send Mail
                    email = Email(subject=_("Authorization code"), from_email=settings.ZB_MAIL_DEFAULT_FROM,
                                  to=[customer_data.get("email")])
                    email.set_text_template("code_mail.txt", email_context)
                    email.set_html_template("code_mail.html", email_context)
                    email.send()
                    cache.set(cache_key, data_cache, settings.CFHL_AUTH_CODE_TIMEOUT * 60)
                    status_return = status.HTTP_200_OK
                else:
                    raise APIException(msg=_("The client id or email is invalid. Please confirm your details at the "
                                             "nearest office and try again."), error=_("Invalid data"),
                                       http_status=status.HTTP_412_PRECONDITION_FAILED)
            else:
                raise ValidationError(_("Data request not found."))
        except CoreValidationError as exc:
            raise APIException(msg=exc.message, error=_("Error at database validations"),
                               http_status=status.HTTP_412_PRECONDITION_FAILED) from exc
        except APIException as exc:
            raise APIException(msg=exc.detail.get("message"), error=exc.detail.get("error"),
                               http_status=exc.status_code) from exc
        except ObjectDoesNotExist as exc:
            raise APIException(msg=_("Customer does not exist."), http_status=status.HTTP_400_BAD_REQUEST)
        except ValidationError as exc:
            raise APIException(msg=_(exc.detail)) from exc
        except Exception as exc:
            raise APIException(msg=_("Not controlled exception error."), error=str(exc)) from exc
        else:
            return Response(status=status_return, data=data_return)

    def user_register(self, request) -> Response:
        return Response(status=status.HTTP_200_OK)
