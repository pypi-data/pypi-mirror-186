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
from oasis_auth.lib.utils import AuthActions
from oasis_auth.lib.utils import SendCode
from rest_framework import status
from rest_framework.response import Response
from uuid import uuid4
from zibanu.django.db.models import ObjectDoesNotExist
from zibanu.django.rest_framework.exceptions import APIException
from zibanu.django.rest_framework.exceptions import ValidationError
from zibanu.django.rest_framework.viewsets import ViewSet
from zibanu.django.utils import CodeGenerator
from zibanu.django.utils import ErrorMessages


class OasisAuthServices(ViewSet):
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
            if {"customer_id", "email", "password"} <= request.data.keys():
                customer = Client.objects.get_customer(request.data.get("customer_id"), request.data.get("email"))
                if customer.is_valid:
                    code_generator = CodeGenerator("pre_register")
                    data_cache = code_generator.generate_dict()
                    data_cache["password"] = request.data.get("password")
                    cache_key = data_cache.pop("uuid").hex
                    customer_data = {
                        "first_name": customer.first_name,
                        "last_name": customer.last_name,
                        "location": customer.location,
                        "address": customer.address,
                        "phone": customer.phone,
                        "mobile": customer.celphone,
                        "email": customer.email,
                        "customer_id": customer.clientid,
                        "document_type": customer.clienttype,
                        "is_valid": customer.is_valid,
                        "type": customer.customer_type,
                    }
                    data_return = {
                        "token": cache_key,
                        "data": customer_data
                    }
                    # Set data cache to store in
                    data_cache["data"] = customer_data
                    # Send Mail
                    email_context = {
                        "customer_name": customer.clientname,
                        "customer_code": data_cache.get("code"),
                        "code_timeout": settings.OASIS_AUTH_CODE_TIMEOUT,
                        "email_datetime": timezone.now().astimezone(tz=timezone.get_default_timezone()).strftime(
                            "%Y-%m-%d %H:%M:%S"),
                        "email_id": str(uuid4())
                    }
                    # Send code mail
                    send_code = SendCode(to=customer_data.get("email"), action=data_cache.get("action"),
                                         context=email_context)
                    if send_code.load_templates():
                        send_code.send()
                    # Store data_cache in cache
                    cache.set(cache_key, data_cache, settings.OASIS_AUTH_CODE_TIMEOUT * 60)
                    status_return = status.HTTP_200_OK
                else:
                    raise APIException(msg=_("The client id or email is invalid. Please confirm your details at the "
                                             "nearest office and try again."), error=_("Invalid data"),
                                       http_status=status.HTTP_412_PRECONDITION_FAILED)
            else:
                raise ValidationError(ErrorMessages.DATA_REQUEST_NOT_FOUND)
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

    def validate_code(self, request) -> Response:
        """
        Method to validate authentication code with token.
        :param request: request object from HTTP
        :return: response object with status and data
        """
        try:
            if request.data and {"token", "code"} <= request.data.keys():
                cache_key = request.data.get("token")
                # Get DataCache
                data_cache = cache.get(cache_key)
                if data_cache:
                    if request.data.get("code") == data_cache.get("code"):
                        auth_action = AuthActions(data_cache)
                        data_result = auth_action.do_action()
                    else:
                        raise ValidationError(_("The code does not match."))
                else:
                    raise ValidationError(_("The code has expired. Please request a new authorization code."))

                status_return = status.HTTP_200_OK
            else:
                raise APIException(ErrorMessages.DATA_REQUEST_NOT_FOUND, "validate_code",
                                   status.HTTP_406_NOT_ACCEPTABLE)
        except ValidationError as exc:
            raise APIException(str(exc)) from exc
        except CoreValidationError as exc:
            raise APIException(msg=exc.message, error="validate_code",
                               http_status=status.HTTP_412_PRECONDITION_FAILED) from exc
        except APIException as exc:
            raise APIException(exc.detail.get("message"), exc.detail.get("detail"), exc.status_code) from exc
        else:
            return Response(status=status_return)
