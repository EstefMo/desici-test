from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.phonebook.models import Address, Person
from apps.phonebook.serializers.address import AddressSerializer


class AddressView(APIView):

    def post(self, request):
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Address created succesfully',
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        address = Address.objects.all()
        return Response(AddressSerializer(address, many=True), status=status.HTTP_200_OK)


class AddressDetailView(APIView):

    def get(self, request, person):
        address = Address.objects.get(person_id=person)
        if address:
            return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        address = Address.objects.get(person=pk)
        if address:
            serializer = AddressSerializer(address, data=request.data)
        else:
            person = Person.objects.get(id=pk)
            serializer = AddressSerializer(data=request.data)
            serializer.person = person
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Address updated succesfully'}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
