from rest_framework import serializers
from apps.phonebook.models import Address

from apps.phonebook.models import Person


class AddressSerializer(serializers.ModelSerializer):
    street_name = serializers.CharField(max_length=255, required=True)
    external_number = serializers.CharField(max_length=10, required=True)
    internal_number = serializers.CharField(max_length=10, required=True)
    settlement = serializers.CharField(max_length=255, required=True)
    district = serializers.CharField(max_length=255, required=True)
    state = serializers.CharField(max_length=3, required=True)
    references = serializers.CharField(max_length=255, required=True)
    person_id = serializers.PrimaryKeyRelatedField(queryset=Person.objects.all()),

    class Meta:
        model = Address
        fields = ('id', 'street_name', 'external_number', 'internal_number',
                  'settlement', 'district', 'state', 'references')
