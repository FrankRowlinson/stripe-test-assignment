from .models import *
from rest_framework import serializers


class ItemSerializer(serializers.ModelSerializer):
    class Meta:    
        model = Item
        fields = (
            "name",
            "description",
            "price"
        )