# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Competition, CompetitionType, Behavior
from .serializers import CompetitionsSerializer, BehaviorSerializer, CompetitionTypeSerializer
from rest_framework.response import Response
from competitions import serializers as competitions_serializer


# Create your views here.

class CompetitionViews(APIView):
    def get(self, request):
        competitions = Competition.objects.all()
        serializers = CompetitionsSerializer(competitions, many=True)
        return Response(serializers.data, status=200)

    def post(self, request, format=None):
        serializer = CompetitionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompetitionDetailsViews(APIView):

    def get_object(self, pk):
        try:
            return Competition.objects.get(pk=pk)
        except Competition.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        competitions = self.get_object(pk)
        serializer = CompetitionsSerializer(competitions)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        competitions = self.get_object(pk)
        serializer = CompetitionsSerializer(competitions, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        competitions = self.get_object(pk)
        competitions.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CompetitionTypeViews(APIView):
    def get(self, request):
        competitions = CompetitionType.objects.all()
        serializers = CompetitionTypeSerializer(competitions, many=True)
        return Response(serializers.data, status=200)


class CompetitionBehaviorViews(APIView):
    # competition with behavior by company
     def get(self, request, pk, format=None):
        competitions = Competition.objects.filter(company=pk)
        serializer = competitions_serializer.CompetitionsBehaviorSerializer(competitions, many=True)
        return Response(serializer.data, status=200)

class CompetitionMejorarViews(APIView):
    # competition by Mejorar
     def get(self, request):
        competitions = Competition.objects.filter(company=2)
        serializer = competitions_serializer.CompetitionsSerializer(competitions, many=True)
        return Response(serializer.data, status=200)

class CompetitionSaveMejorarViews(APIView):
    # competition by Mejorar
     def post(self, request, format=None):
        serializer = CompetitionsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CompetitionBehaviorMejorarViews(APIView):
    # competition by Mejorar
     def get(self, request):
        competitions = Competition.objects.filter(company=2)
        serializer = competitions_serializer.CompetitionsBehaviorSerializer(competitions, many=True)
        return Response(serializer.data, status=200)

class BehaviorViews(APIView):

    def get(self, request):
        behaviors = Behavior.objects.all()
        serializers = BehaviorSerializer(behaviors, many=True)
        return  Response(serializers.data, status=200)

    def post(self, request, format=None):
        serializer = BehaviorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class BehaviorDetailsViews(APIView):

    def get_object(self, pk):
        try:
            return Behavior.objects.get(pk=pk)
        except Behavior.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        behaviors = self.get_object(pk)
        serializer = BehaviorSerializer(behaviors)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        behavior = self.get_object(pk)
        serializer = BehaviorSerializer(behavior, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        behavior = self.get_object(pk)
        behavior.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
