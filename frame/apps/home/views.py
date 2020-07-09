# Create your views here.
from rest_framework.generics import ListAPIView

from frame.apps.home.models import Banner
from frame.apps.home.serializers import BannerModelSerializer


class BannerListAPIView(ListAPIView):
    queryset = Banner.objects.filter(is_show=True, is_delete=False).order_by("-orders")
    serializer_class = BannerModelSerializer
