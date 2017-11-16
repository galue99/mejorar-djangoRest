__author__ = 'edgar'
from rest_framework import serializers
from polls.models import Poll, PollUser, Level
from items.models import Item
from items.serializers import ItemSerializer

class PollSerializer(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    class Meta:
        model = Poll
        fields = '__all__'

class PollCrudSerializer(serializers.ModelSerializer):
    #items = ItemSerializer(many=True)
    class Meta:
        model = Poll
        fields = '__all__'

class PollUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollUser
        fields = '__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = '__all__'