from rest_framework import serializers
from .models import *


class PlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platform
        fields = ['id', 'name']


class ChannelSerializer(serializers.ModelSerializer):
    platform = PlatformSerializer(many=False, read_only=True)
    class Meta:
        model = Channel
        fields = ['id', 'name', 'platform']


class ConfigSerializer(serializers.ModelSerializer):
    resource = ChannelSerializer(many=True, read_only=True)
    platform_count = serializers.SerializerMethodField()

    class Meta:
        model = Config
        fields = ['resource', 'platform_count']

    def get_platform_count(self, obj):
        # @todo: Wrong platform number: Calculation must be corrected
        return Platform.objects.filter(active=True).count()
