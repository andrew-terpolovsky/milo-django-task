from django.conf.urls import url, include
from rest_framework import routers

from .views import UsersViewSet, index, export_csv

router = routers.SimpleRouter()
router.register(r'user', UsersViewSet)

urlpatterns = [
    url(
        regex=r'^$',
        view=index,
        name='home'
    ),
    url(
        regex=r'^export/$',
        view=export_csv,
        name='export-csv'
    ),
    url(r'^', include(router.urls)),
]