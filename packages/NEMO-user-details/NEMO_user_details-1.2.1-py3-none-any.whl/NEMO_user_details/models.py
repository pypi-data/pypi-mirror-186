from NEMO.models import BaseModel, User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models


class Ethnicity(BaseModel):
    name = models.CharField(max_length=200, unique=True, help_text="The name of the ethnicity")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Ethnicities"
        ordering = ["name"]


class Race(BaseModel):
    name = models.CharField(max_length=200, unique=True, help_text="The name of the race")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class Gender(BaseModel):
    name = models.CharField(max_length=200, unique=True, help_text="The name of the gender")

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]


class UserDetails(BaseModel):
    user = models.OneToOneField(User, related_name="details", on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, null=True, blank=True, help_text="The user's gender", on_delete=models.SET_NULL)
    race = models.ForeignKey(Race, null=True, blank=True, help_text="The user's race", on_delete=models.SET_NULL)
    ethnicity = models.ForeignKey(
        Ethnicity, null=True, blank=True, help_text="The user's ethnicity", on_delete=models.SET_NULL
    )
    emergency_contact = models.CharField(
        max_length=250, blank=True, help_text="The user's emergency contact information"
    )
    phone_number = models.CharField(max_length=40, blank=True, help_text="The user's phone number")
    rate_category_type = models.ForeignKey(ContentType, null=True, blank=True, on_delete=models.CASCADE)
    rate_category_id = models.PositiveIntegerField(null=True, blank=True)
    rate_category = GenericForeignKey("rate_category_type", "rate_category_id")

    def __str__(self):
        return f"{self.user.get_name()}'s details"
