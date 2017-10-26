import csv

from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet

from .models import User
from .serializers import UserSerializer
from .templatetags.manage_user import bizz_fuzz, allowed


class UsersViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)


def index(request):
    return render(request, 'index.html', {
        'users': User.objects.filter(is_superuser=False)
    })


def export_csv(request):
    users = User.objects.filter(is_superuser=False)
    response = HttpResponse()
    response['Content-Type'] = 'text/csv'
    response['Content-Disposition'] = 'attachment; filename="users.CSV"'
    writer = csv.writer(response, delimiter=',', quoting=csv.QUOTE_MINIMAL)
    writer.writerow([
        'Username',
        'Birthday',
        'Eligible',
        'Random Number',
        'BizzFuzz'
    ])
    for user in users:
        writer.writerow([
            user.username,
            user.birthday or 'N/A',
            allowed(user.birthday) or 'N/A',
            user.rand_num,
            bizz_fuzz(user.rand_num)
        ])
    return response
