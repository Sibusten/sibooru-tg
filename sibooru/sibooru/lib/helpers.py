# -*- coding: utf-8 -*-
"""Template Helpers used in sibooru."""
import logging
from datetime import datetime

from markupsafe import Markup

log = logging.getLogger(__name__)


def current_year():
    now = datetime.now()
    return now.strftime('%Y')


def icon(icon_name):
    return Markup('<i class="glyphicon glyphicon-%s"></i>' % icon_name)


# Import commonly used helpers from WebHelpers2 and TG

try:
    from webhelpers2 import date, html, number, misc, text
except SyntaxError:
    log.error("WebHelpers2 helpers not available with this Python Version")
