# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, permissions, status, views
from rest_framework.views import APIView
from .models import Poll, PollUser, Level
from polls import serializers as polls_serializers
# Create your views here.

"""
    poll list
"""
class PollsViews(APIView):

    def get(self, request, *args, **kwargs):
        polls = Poll.objects.all()
        serializer = polls_serializers.PollSerializer(polls, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None, aux1=None):

        aux = request.data
        serializer = polls_serializers.PollCrudSerializer(data=aux)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    poll detail
"""

class PollDetail(APIView):

    def get_object(self, pk):
        try:
            return Poll.objects.get(pk=pk)
        except Poll.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = polls_serializers.PollSerializer(poll)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = polls_serializers.PollSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
    poll user list
"""
class PollUserViews(APIView):

    def get(self, request, *args, **kwargs):
        polls = PollUser.objects.all()
        serializer = polls_serializers.PollUserSerializer(polls, many=True)
        return Response(serializer.data, status=200)

    def post(self, request, format=None):
        serializer = polls_serializers.PollUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
    poll user-detail
"""
class PollUserDetail(APIView):

    def get_object(self, pk):
        try:
            return PollUser.objects.get(pk=pk)
        except PollUser.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = polls_serializers.PollUserSerializer(poll)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        poll = self.get_object(pk)
        serializer = polls_serializers.PollUserSerializer(poll, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        poll = self.get_object(pk)
        poll.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

"""
    Level List
"""
class LevelViews(APIView):

    def get(self, request, *args, **kwargs):
        levels = Level.objects.all()
        serializer = polls_serializers.LevelSerializer(levels, many=True)
        return Response(serializer.data, status=200)