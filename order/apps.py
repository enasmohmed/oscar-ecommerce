from django.utils.translation import gettext_lazy as _

from oscar.core.application import OscarConfig


class OrderConfig(OscarConfig):
    label = 'order'
    name = 'order'
    verbose_name = _('Order')
