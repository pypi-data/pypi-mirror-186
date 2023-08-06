from NEMO.admin import UserAdmin
from NEMO.models import User
from django.contrib import admin

from NEMO_user_details.forms import UserDetailsAdminForm
from NEMO_user_details.models import Ethnicity, Gender, Race, UserDetails


class UserDetailsInline(admin.StackedInline):
    form = UserDetailsAdminForm
    model = UserDetails
    can_delete = False


class NewUserAdmin(UserAdmin):
    inlines = (UserDetailsInline,) + UserAdmin.inlines


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, NewUserAdmin)

admin.site.register(Race)
admin.site.register(Gender)
admin.site.register(Ethnicity)
