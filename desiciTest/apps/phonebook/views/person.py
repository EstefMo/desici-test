from django.forms import model_to_dict
from django.http import HttpResponse
from django.urls import reverse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from django.core import serializers
from django.shortcuts import redirect, render

from apps.phonebook.models import Person
from apps.phonebook.serializers.person import PersonSerializer
from apps.phonebook.views.address import AddressDetailView
from apps.phonebook.views.phone import PhoneDetailView


class PersonEditPage(APIView):
    def get(self, request, pk):
        person = PersonDetailView.get(self, request, pk)
        address = AddressDetailView.get(self, request, pk)
        phone = PhoneDetailView.get(self, request, pk)
        return render(request, 'edit_person.html',
                      {"person": person.data, "address": address.data if address else [], "numbers": phone.data})

    def put(self, request, pk):
        serializer = PersonSerializer(Person.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Person updated succesfully',
                             'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


class PersonRenderPage(APIView):
    def get(self, request):
        return render(request, 'form_add_person.html')

    def post(self, request):
        response = PersonView.post(self, request)
        if "data" in response.data:
            return redirect('person_edit_page', pk=response.data['data']['id'])
        return render(request, 'form_add_person.html', {"error":response.data["message"] })


class PersonView(APIView):

    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        persons = Person.objects.all()
        return render(request, 'index.html', {'persons': PersonSerializer(persons, many=True).data})


class PersonDetailView(APIView):

    def get(self, request, pk):
        person = Person.objects.get(pk=pk)
        if person:
            return Response(PersonSerializer(person).data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        serializer = PersonSerializer(Person.objects.get(pk=pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Person updated succesfully',
                             'data': serializer.data}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        person = Person.objects.get(pk=pk)
        if person:
            Person.objects.get(pk=pk).delete()
            return Response(status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
