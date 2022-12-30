from rest_framework import serializers
from apps.phonebook.models import Phone


class PhoneSerializer(serializers.ModelSerializer):
    type = serializers.IntegerField(required=True)
    alias = serializers.CharField(max_length=10, required=True)
    number = serializers.CharField(max_length=50, required=True)

    class Meta:
        model = Phone
        fields = ('id', 'type', 'alias', 'number', 'person')

