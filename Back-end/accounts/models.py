from django.db import models

from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.core.validators import RegexValidator
from django.contrib.auth.hashers import make_password, check_password
from django_countries.fields import CountryField

class CustomUser(AbstractUser):

    country=CountryField(blank=True, null=True)  # Country field
    city = models.CharField(max_length=100, blank=True)  # City field
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message=_("Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)  # Phone number field
    day_of_birth = models.DateField(null=True, blank=True)  # Date of birth field

    address = models.CharField(max_length=255, blank=True)  # Address field

