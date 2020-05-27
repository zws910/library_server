from django.conf.urls import url
from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from .views import *

urlpatterns = [
    url(r'^mobiles/count/$', MobileCountView.as_view()),
    url(r'^login/account', obtain_jwt_token),
    url(r'^currentUser', CurrentUserView.as_view())
]