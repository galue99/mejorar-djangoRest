__author__ = 'edgar'
from rest_framework import serializers
from .models import Item, Phrase
from competitions.serializers import CompetitionTypeSerializer

class PhraseV2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Phrase
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    competition_type = CompetitionTypeSerializer(read_only=True)
    competition_type_id = serializers.IntegerField(required=True)
    phrases = PhraseV2Serializer(many=True)
    class Meta:
        model = Item
        fields = '__all__'

class PhraseSerializer(serializers.ModelSerializer):
    item = ItemSerializer(read_only=True)
    item_id = serializers.IntegerField(required=True)
    class Meta:
        model = Phrase
        fields = '__all__'