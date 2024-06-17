from dataclasses import fields
from django.contrib.auth.models import Group, User
from rest_framework import serializers

from students.models import Student
#from .models import student

#from tutorial.quickstart.models import student

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']



