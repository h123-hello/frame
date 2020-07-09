from rest_framework import serializers

from frame.apps.home.models import Banner


class BannerModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ("img", 'link')
