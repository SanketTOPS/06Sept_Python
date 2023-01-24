from rest_framework import serializers
from .models import userinfo

class userSerializers(serializers.ModelSerializer):
    class Meta:
        model=userinfo
        fields='__all__'