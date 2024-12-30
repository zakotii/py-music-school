from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models


class Musician(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    instrument = models.CharField(max_length=63)
    age = models.IntegerField(null=True, blank=True)
    date_of_applying = models.DateField(auto_now_add=True)

    def clean(self):
        if self.age is not None and self.age < 14:
            raise ValidationError(
                {"age": _("Age must be at least 14.")}
            )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_adult(self):
        return self.age is not None and self.age >= 21
