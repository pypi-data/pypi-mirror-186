# -*- coding: utf-8 -*-

#  Developed by CQ Inversiones SAS. Copyright ©. 2019 - 2022. All rights reserved.
#  Desarrollado por CQ Inversiones SAS. Copyright ©. 2019 - 2022. Todos los derechos reservado

# ****************************************************************
# IDE:          PyCharm
# Developed by: macercha
# Date:         20/12/22 2:35 PM
# Project:      CFHL Transactional Backend
# Module Name:  mail
# Description:
# ****************************************************************
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.exceptions import TemplateSyntaxError
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.utils.translation import gettext_lazy as _
from typing import Any
from uuid import uuid4


class Email(EmailMultiAlternatives):
    """
    Override EmailMultiAlternatives class for create an email from html template and html text.
    """

    def __init__(self, subject: str = "", body: str = "", from_email: str = None, to: list = None, bcc: list = None,
                 connection: Any = None, attachments: list = None, headers: dict = None, cc: list = None,
                 reply_to: list = None):
        # Define message id for unique id
        self.__text_content = None
        self.__html_content = None
        self.__message_id = uuid4().hex
        # Set default values
        from_email = from_email if from_email is not None else settings.ZB_MAIL_DEFAULT_FROM
        reply_to = reply_to if reply_to is not None else [settings.ZB_MAIL_REPLY_TO]
        # Analyze errors
        cc = cc if cc is not None else []
        if headers is None:
            headers = {
                "Message-ID": self.__message_id
            }
        else:
            headers["Message-ID"] = self.__message_id
        super().__init__(subject=subject, body=body, from_email=from_email, to=to, bcc=bcc, connection=connection,
                         attachments=attachments, headers=headers, cc=cc, reply_to=reply_to)

    def __get_template_content(self, template: str, context: dict = None) -> Any:
        """
        Return content from template after render with context if case.
        :param template: template file
        :param context: context vars for template
        :return:
        """
        try:
            template = get_template(template_name=template)
            if context is not None:
                template_content = template.render(context)
            else:
                template_content = template.render()
        except TemplateSyntaxError:
            raise TemplateSyntaxError(_("Syntax error loading template '{}'").format(template))
        except TemplateDoesNotExist:
            raise TemplateDoesNotExist(_("Template '{}' does not exist.").format(template))
        else:
            return template_content

    def set_text_template(self, template: str, context: dict = None):
        self.body = self.__get_template_content(template=template, context=context)

    def set_html_template(self, template: str, context: dict = None):
        self.attach_alternative(self.__get_template_content(template=template, context=context), "text/html")
