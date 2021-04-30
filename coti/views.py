from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView

from coti.models import TColor, TInstallation, TPayment
from coti.serializers import TColorSerializer, TInstallationSerializer, TPaymentSerializer


class TColorList(ListAPIView):
    queryset = TColor.objects.all()
    serializer_class = TColorSerializer


class TInstallationList(ListAPIView):
    queryset = TInstallation.objects.all()
    serializer_class = TInstallationSerializer


class TPaymentList(ListAPIView):
    queryset = TPayment.objects.all()
    serializer_class = TPaymentSerializer
