from django.db.models import fields
from rest_framework import serializers, fields
from .models import Client, User, Project




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','name')



class ClientSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_created_by(self, obj):
        return getattr(obj, 'created_by', 'Rohit')

    def get_created_at(self, obj):
        return getattr(obj, 'created_at', '')

    class Meta:
        model=Client
        fields=('id', 'client_name', 'created_at', 'created_by', )




class ProjectSerializer(serializers.ModelSerializer):
    created_at = serializers.SerializerMethodField()
    created_by = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()



    def get_created_at(self, obj):
        return getattr(obj, 'created_at', '2019-12-24T11:03:55.931739+05:30')

    def get_created_by(self, obj):
        return getattr(obj, 'created_by', 'Ganesh')


    def get_updated_at(self, obj):
        return getattr(obj, 'updated_at', '2019-12-24T11:03:55.931739+05:30')



    class Meta:
        model = Project
        fields = ('id', 'project_name','created_at','created_by','updated_at')

      
  
  