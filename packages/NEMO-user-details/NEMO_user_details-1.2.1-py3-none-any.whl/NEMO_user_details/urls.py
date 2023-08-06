from NEMO.urls import router
from django.urls import re_path

from NEMO_user_details import api, views

router.register(r"users_with_details", api.UserWithDetailsViewSet)

urlpatterns = [
	# Override modify user page to add user details fields
    re_path(r"^user/(?P<user_id>\d+|new)/", views.create_or_modify_user_and_details, name='create_or_modify_user_and_details'),
]