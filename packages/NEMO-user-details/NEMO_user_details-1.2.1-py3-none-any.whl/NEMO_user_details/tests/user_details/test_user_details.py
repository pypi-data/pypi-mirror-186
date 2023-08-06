from NEMO.models import User
from django.apps import apps
from django.test import TestCase
from django.urls import reverse

from NEMO_user_details.customizations import UserDetailsCustomization
from NEMO_user_details.forms import UserDetailsForm


field_names = ["emergency_contact", "phone_number", "race", "gender", "ethnicity"]


class TestUserDetails(TestCase):
    def test_url(self):
        user, created = User.objects.get_or_create(
            username="test_user", first_name="Testy", last_name="McTester", badge_number=1, is_user_office=True
        )
        self.client.force_login(user)
        response = self.client.get(reverse("create_or_modify_user", args=[1]), follow=True)
        for field_name in field_names:
            self.assertNotContains(response, f'name="{field_name}"')
        self.assertEqual(response.status_code, 200)
        # Set fields
        for field_name in field_names:
            UserDetailsCustomization.set(f"user_details_enable_{field_name}", "enabled")
        response = self.client.get(reverse("create_or_modify_user", args=[1]), follow=True)
        for field_name in field_names:
            self.assertContains(response, f'name="{field_name}"')
        self.assertEqual(response.status_code, 200)

    def test_form_fields(self):
        for field_name in field_names:
            test_form_field(self, field_name)

    def test_rate_category(self):
        if apps.is_installed("NEMO_billing.rates"):
            print("Testing with billing")
            test_form_field(self, "rate_category")
        else:
            print("Testing without billing")
            # No matter the options set, it should always be disabled
            # and not required if the billing plugin is not installed
            UserDetailsCustomization.set("user_details_enable_rate_category", "enabled")
            UserDetailsCustomization.set("user_details_require_rate_category", "enabled")
            form = UserDetailsForm()
            self.assertTrue(form.fields["rate_category"].disabled)
            self.assertFalse(form.fields["rate_category"].required)


def test_form_field(test_case: TestCase, field_name):
    # By default fields are not enabled
    form = UserDetailsForm()
    test_case.assertTrue(form.fields[field_name].disabled)
    test_case.assertFalse(form.fields[field_name].required)
    # Requires means enable and required
    UserDetailsCustomization.set(f"user_details_require_{field_name}", "enabled")
    form = UserDetailsForm()
    test_case.assertFalse(form.fields[field_name].disabled)
    test_case.assertTrue(form.fields[field_name].required)
    # Reset required part
    UserDetailsCustomization.set(f"user_details_require_{field_name}", "")
    # Set enabled only
    UserDetailsCustomization.set(f"user_details_enable_{field_name}", "enabled")
    form = UserDetailsForm()
    test_case.assertFalse(form.fields[field_name].disabled)
    test_case.assertFalse(form.fields[field_name].required)
