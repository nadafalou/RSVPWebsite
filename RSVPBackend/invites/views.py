from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404 

from invites.serializers import GuestSerializer, CreateGuestSerializer, UpdateGuestSerializer
from invites.models import Guest

# Create your views here.

class GuestInvite(generics.RetrieveAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    permission_classes = (permissions.AllowAny,)

class CreateGuestInvite(generics.CreateAPIView):
    queryset = Guest.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateGuestSerializer

class UpdateGuestInvite(generics.UpdateAPIView):
    queryset = Guest.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UpdateGuestSerializer

    def get_object(self):
        return get_object_or_404(Guest, id=self.kwargs.get('pk'))

class GuestInvites(generics.ListAPIView):
    queryset = Guest.objects.all()
    serializer_class = GuestSerializer
    model = serializer_class.Meta.model
    # paginate_by = 100
    permission_classes = [permissions.AllowAny,] 