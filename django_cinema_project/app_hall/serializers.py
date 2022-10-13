from rest_framework import serializers
from .models import Hall


class HallSerializer(serializers.ModelSerializer):

    class Meta:
        model = Hall
        fields = ('id', 'number', 'max_people_count')