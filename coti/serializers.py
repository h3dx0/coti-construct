
from rest_framework import serializers

from coti.models import TColor, Accessory, Complement, TInstallation


class TInstallationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TInstallation
        fields = '__all__'


class TColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = TColor
        fields = '__all__'


class AccessorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Accessory
        fields = '__all__'


class ComplementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complement
        fields = '__all__'
