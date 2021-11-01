from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    # create serializer
    class Meta:
        model = Person
        fields = (
            "first_name",
            "last_name",
            "gender",
            "height",
            "weight",
            "birthdate",
            "district",
            "state",
            "number",
        )
