import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext as _

class SymbolValidator(object):
    def validate(self, password, user=None):
        if not re.findall('[()[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("La contraseña debe contener por lo menos un símbolo: " +
                  "( ) [ ] { } | \ ` ~ ! @ # $ % ^ & * _ - + = ; : ' \" , < > . / ?"),
                code='password_no_symbol',
            )
    
    def get_help_text(self):
        return _(
            "La contraseña debe contener por lo menos un símbolo: " +
            "( ) [ ] { } | \ ` ~ ! @ # $ % ^ & * _ - + = ; : ' \" , < > . / ?"
        )