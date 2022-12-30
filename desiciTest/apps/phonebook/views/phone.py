from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.core import serializers

from apps.phonebook.models import Phone
from apps.phonebook.serializers.phone import PhoneSerializer

from apps.phonebook.models import Person


class PhoneView(APIView):

    def post(self, request):
        serializer = PhoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return redirect('person_edit_page', pk=request.data['person'])
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        phones = Phone.objects.all()
        return Response(PhoneSerializer(phones, many=True), status=status.HTTP_200_OK)


class PhoneDetailView(APIView):

    def get(self, request, person):
        phone = Phone.objects.filter(person=person)
        if phone:
            return Response(PhoneSerializer(phone, many=True).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        phone = Phone.objects.get(id=pk)
        if phone:
            serializer = PhoneSerializer(phone, data=request.data)
            person = Person.objects.get(id=request.data['person'])
           
            serializer.person = person
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Phone updated succesfully'}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        phone = Phone.objects.get(pk=pk)
        if phone:
            Phone.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)