from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.phonebook.models import Address, Person
from apps.phonebook.serializers.address import AddressSerializer


class AddressView(APIView):

    def post(self, request):
        person = Person.objects.get(id=request.data['person_id'])
        serializer = AddressSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(person=person)
            return Response({'message': 'Address created succesfully',
                             'data': serializer.data}, status=status.HTTP_201_CREATED)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        address = Address.objects.all()
        return Response(AddressSerializer(address, many=True), status=status.HTTP_200_OK)


class AddressDetailView(APIView):

    def get(self, request, person):
        if Address.objects.filter(person=person).exists():
            address = Address.objects.get(person=person)
            return Response(AddressSerializer(address).data, status=status.HTTP_200_OK)
        return Response([], status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        if Address.objects.filter(person=pk).exists():
            address = Address.objects.get(person=pk)
            serializer = AddressSerializer(address, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Address updated succesfully'}, status=status.HTTP_200_OK)
        return Response({'message': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
