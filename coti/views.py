from django.shortcuts import render

# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from coti.models import TColor, TInstallation, TPayment, Client, Accessory, Complement
from coti.permissions import BearerTokenAuth
from coti.serializers import TColorSerializer, TInstallationSerializer, TPaymentSerializer, ClientSerializer, \
    AccessorySerializer, ComplementsSerializer


class ClientListCreate(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        client = Client()
        client.first_name = request.data['first_name']
        client.last_name = request.data['last_name']
        client.email = request.data['email']
        client.username = request.data['email']
        client.set_password('*AgEnErAtEpAsSwOrD*')
        client.telephone = request.data['telephone']
        client.catchment = request.data['catchment']
        client.street = request.data['street']
        client.out_number = request.data['out_number']
        client.int_number = request.data['int_number']
        client.cp = request.data['cp']
        client.colony = request.data['colony']
        client.municipality = request.data['municipality']
        client.state = request.data['state']
        client.save(client)
        serializer = ClientSerializer(client)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ClientRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        client = Client.objects.get(pk=self.kwargs['pk'])
        client.first_name = request.data['first_name']
        client.last_name = request.data['last_name']
        client.email = request.data['email']
        client.username = request.data['email']
        client.telephone = request.data['telephone']
        client.catchment = request.data['catchment']
        client.street = request.data['street']
        client.out_number = request.data['out_number']
        client.int_number = request.data['int_number']
        client.cp = request.data['cp']
        client.colony = request.data['colony']
        client.municipality = request.data['municipality']
        client.state = request.data['state']
        client.save()
        serializer = ClientSerializer(client)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class TColorList(ListAPIView):
    queryset = TColor.objects.all()
    serializer_class = TColorSerializer
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]


class TInstallationList(ListAPIView):
    queryset = TInstallation.objects.all()
    serializer_class = TInstallationSerializer
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]


class TPaymentList(ListAPIView):
    queryset = TPayment.objects.all()
    serializer_class = TPaymentSerializer
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]


class AccessoryList(ListAPIView):
    queryset = Accessory.objects.all()
    serializer_class = AccessorySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profile']
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]


class ComplementsList(ListAPIView):
    queryset = Complement.objects.all()
    serializer_class = ComplementsSerializer
    authentication_classes = [BearerTokenAuth]
    permission_classes = [IsAuthenticated]
