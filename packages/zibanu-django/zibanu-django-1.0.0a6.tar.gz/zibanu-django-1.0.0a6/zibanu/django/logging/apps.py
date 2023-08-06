# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         10/12/22 10:23 AM
# Project:      CFHL Transactional Backend
# Module Name:  apps
# Description:
# ****************************************************************
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ZibanuLogging(AppConfig):
    default_auto_field = "django.db.models.AutoField"
    name = "zibanu.django.logging"
    verbose_name = _("Zibanu Logging")

