__author__ = 'edgar'
from rest_framework import serializers
from .models import Competition, Behavior, CompetitionType
from accounts.serializers import CompanySerializer

class CompetitionTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompetitionType
        fields = '__all__'

class CompetitionsSerializer(serializers.ModelSerializer):
    type = CompetitionTypeSerializer(read_only=True)
    type_id = serializers.IntegerField(required=True)
    company = CompanySerializer(read_only=True)
    company_id = serializers.IntegerField(required=True)
    class Meta:
        model = Competition
        fields = '__all__'

class BehaviorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Behavior
        fields = '__all__'

class CompetitionsBehaviorSerializer(serializers.ModelSerializer):
    behaviors = BehaviorSerializer(many=True)
    class Meta:
        model = Competition
        fields = ('__all__')
