from rest_framework import serializers
from apps.phonebook.models import Person


class PersonSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, required=True)
    last_name = serializers.CharField(max_length=120, required=True)
    birth_date = serializers.DateField(required=False)
    picture = serializers.CharField(max_length=100, required=True)

    class Meta:
        model = Person
        fields = ('id', 'name', 'last_name', 'picture', 'birth_date')