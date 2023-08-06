from django.apps import apps
from django.contrib.auth.models import Group
from django.forms import HiddenInput, ModelChoiceField, ModelMultipleChoiceField, models

from NEMO_user_details.customizations import UserDetailsCustomization
from NEMO_user_details.models import UserDetails
from NEMO_user_details.utilities import is_billing_rates_installed


# Base details form for admin. We are setting disabled and required attributes here
class UserDetailsAdminForm(models.ModelForm):
    rate_category = ModelChoiceField(queryset=Group.objects.none(), required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        disable_fields, require_fields = UserDetailsCustomization.disable_require_fields()
        if "rate_category" not in disable_fields:
            self.fields["rate_category"].queryset = apps.get_model("rates", "RateCategory").objects.all()
            if self.instance.pk and self.instance.rate_category:
                self.fields["rate_category"].initial = self.instance.rate_category
        for field_name in require_fields:
            if field_name in self.fields:
                self.fields[field_name].required = True
        for field_name in disable_fields:
            if field_name in self.fields:
                self.fields[field_name].disabled = True
                self.fields[field_name].required = False
                self.fields[field_name].widget = HiddenInput()

    def save(self, commit=True):
        if is_billing_rates_installed():
            self.instance.rate_category = self.cleaned_data["rate_category"]
        return super().save(commit=commit)

    class Meta:
        model = UserDetails
        exclude = ["user", "rate_category_type", "rate_category_id"]


# Details form for users page (groups are already on the admin form for users, but we need to add them explicitly here)
class UserDetailsForm(UserDetailsAdminForm):
    groups = ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        required=False,
    )

    def save(self, commit=True):
        details: UserDetails = super().save(commit=commit)
        if UserDetailsCustomization.get_bool("user_details_enable_groups"):
            details.user.groups.set(self.cleaned_data["groups"])
        return details
