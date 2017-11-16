__author__ = 'edgar'
from rest_framework import serializers
from accounts.models import User, Company, Rol
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'name',
            'url'
        )

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = (
            'id',
            'name',
        )

class UserSerializer(serializers.ModelSerializer):
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(required=True)
    rol = RolSerializer(read_only=True)
    rol_id = serializers.IntegerField(required=True)
    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'password',
            'first_name',
            'last_name',
            'email',
            'dni',
            'position',
            'branch_office',
            'rol',
            'rol_id',
            'company',
            'company_id',
        )
        extra_kwargs = {
            'password': {'read_only': True},
        }