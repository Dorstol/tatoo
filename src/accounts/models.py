from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models
from django.utils.translation import gettext as _
from phonenumber_field.modelfields import PhoneNumberField

from accounts.managers import CustomerManager


class Customer(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    first_name = models.CharField(_("first name"), max_length=156, blank=True)
    last_name = models.CharField(_("last name"), max_length=156, blank=True)
    birthdate = models.DateField(_("birthday"), null=True, blank=True)
    is_tattoo_master = models.BooleanField(default=False, blank=True)
    phone = PhoneNumberField(
        _("Phone number"), null=True, blank=True, validators=[RegexValidator(r"^\d{3}-\d{3}-\d{4}$")]
    )

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. " "Unselect this instead of deleting accounts."
        ),
    )

    photo = models.ImageField(upload_to="users_photo/", null=True, blank=True)

    objects = CustomerManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("Customer")
        verbose_name_plural = _("Customers")

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)
