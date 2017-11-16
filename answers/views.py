# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import render
from .models import Answer, UserAnswer
from .serializers import AnswerSerializer, UserAnswerSerializer
from rest_framework.response import Response


# Create your views here.

class AnswersViews(APIView):
    def get(self, request):
        answers = Answer.objects.all()
        serializers = AnswerSerializer(answers, many=True)
        return Response(serializers.data, status=200)

    def post(self, request, format=None):
        serializer = AnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AnswerViewsDetail(APIView):

    def get_object(self, pk):
        try:
            return Answer.objects.get(pk=pk)
        except Answer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        answer = self.get_object(pk)
        serializer = AnswerSerializer(answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        answer = self.get_object(pk)
        answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAnswerViews(APIView):

    def get(self, request):
        user_answer = UserAnswer.objects.all()
        serializers = UserAnswerSerializer(user_answer, many=True)
        return Response(serializers.data, status=200)

    def post(self, request, format=None):
        serializer = UserAnswerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserAnswerDetailViews(APIView):
    def get_object(self, pk):
        try:
            return UserAnswer.objects.get(pk=pk)
        except UserAnswer.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        user_answer = self.get_object(pk)
        serializer = UserAnswerSerializer(user_answer)
        return Response(serializer.data, status=200)

    def put(self, request, pk, format=None):
        user_answer = self.get_object(pk)
        serializer = UserAnswerSerializer(user_answer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user_answer = self.get_object(pk)
        user_answer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)