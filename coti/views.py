from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from coti.models import TColor
from coti.serializers import TColorSerializer


class TColorList(ListAPIView):
    queryset = TColor.objects.all()
    serializer_class = TColorSerializer
