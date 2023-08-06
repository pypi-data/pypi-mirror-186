# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         20/12/22 12:42 PM
# Project:      CFHL Transactional Backend
# Module Name:  urls
# Description:
# ****************************************************************
from oasis_auth.api import services
from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()

urlpatterns = [
    path(r"", include(routers.get_urls())),
    path(r"pre-register/", services.CfhlAuth.as_view({"post": "pre_register"}))
]
