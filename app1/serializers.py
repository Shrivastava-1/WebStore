from rest_framework import serializers
from .models import Allitems

class ClassSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True)
    class Meta:
        model = Allitems
        fields = ['name', 'rate', 'field', 'quality', 'image']