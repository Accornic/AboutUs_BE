from rest_framework import serializers
from .models import(
    BlogContent
)

class  BlogContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogContent
        fields = ('__all__')