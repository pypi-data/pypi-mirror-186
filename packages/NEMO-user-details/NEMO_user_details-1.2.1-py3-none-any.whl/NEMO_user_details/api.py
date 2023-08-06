from NEMO.models import User
from NEMO.serializers import UserSerializer
from NEMO.views.api import UserViewSet
from rest_framework.fields import CharField
from rest_framework.serializers import ModelSerializer

from NEMO_user_details.customizations import UserDetailsCustomization
from NEMO_user_details.models import UserDetails


class UserDetailsSerializer(ModelSerializer):
    billing_rate = CharField(source="rate_category.name", default=None)
    gender = CharField(source="gender.name", default=None)
    race = CharField(source="race.name", default=None)
    ethnicity = CharField(source="ethnicity.name", default=None)

    def get_fields(self):
        fields = super().get_fields()
        disable_fields, require_fields = UserDetailsCustomization.disable_require_fields()
        for disable_field in disable_fields:
            if disable_field in fields:
                del fields[disable_field]
        return fields

    class Meta:
        model = UserDetails
        exclude = ("user", "rate_category_type", "rate_category_id")


class UserWithDetailsSerializer(UserSerializer):
    details = UserDetailsSerializer(required=False)

    def get_fields(self):
        fields = super().get_fields()
        detail_fields = fields.pop("details")
        if detail_fields:
            for key, value in detail_fields.fields.items():
                if key != "id":
                    # reset the source to details
                    value.source = "details." + value.source
                    value.source_attrs = value.source.split(".")
                    fields[key] = value
        return fields

    class Meta:
        model = User
        exclude = (
            "user_permissions",
            "qualifications",
            "physical_access_levels",
            "preferences",
            "projects",
            "managed_projects",
        )


class UserWithDetailsViewSet(UserViewSet):
    serializer_class = UserWithDetailsSerializer
