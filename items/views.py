# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404

from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Item, Phrase
from .serializers import ItemSerializer, PhraseSerializer


class ItemViews(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializers = ItemSerializer(items, many=True)
        return Response(serializers.data, status=200)

    def post(self, request, format=None):
        serializer = ItemSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def saveBehavior(self, data):
        print(data)

class ItemDetailsViews(APIView):

    def get_object(self, pk):
        try:
            return Item.objects.get(pk=pk)
        except Item.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        item = self.get_object(pk)
        serializer = ItemSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        item = self.get_object(pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PhraseViews(APIView):
    def get(self, request):
        phrases = Phrase.objects.all()
        serializers = PhraseSerializer(phrases, many=True)
        return Response(serializers.data, status=200)

    def post(self, request, format=None):
        serializer = PhraseSerializer(data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PhraseDetailsViews(APIView):

    def get_object(self, pk):
        try:
            return Phrase.objects.get(pk=pk)
        except Phrase.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        phrase = self.get_object(pk)
        serializer = PhraseSerializer(phrase)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        phrase = self.get_object(pk)
        serializer = PhraseSerializer(phrase, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        phrase = self.get_object(pk)
        phrase.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)