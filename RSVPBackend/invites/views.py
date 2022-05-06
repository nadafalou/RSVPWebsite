from django.shortcuts import render
from rest_framework import generics
from rest_framework import permissions
from django.shortcuts import get_object_or_404 

from invites.serializers import (
    InviteSerializer, CreateInviteSerializer, 
    UpdateInviteSerializer, EventSerializer,
    CreateEventSerializer
)
from invites.models import Invite, Event

# Create your views here.

class InviteView(generics.RetrieveAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    permission_classes = (permissions.AllowAny,)

class EventView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = (permissions.AllowAny,)

class CreateInviteView(generics.CreateAPIView):
    queryset = Invite.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateInviteSerializer

class CreateEventView(generics.CreateAPIView):
    queryset = Event.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = CreateEventSerializer

class UpdateInviteView(generics.UpdateAPIView):
    queryset = Invite.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = UpdateInviteSerializer

    def get_object(self):
        return get_object_or_404(Invite, id=self.kwargs.get('pk'))

class ListInvitesView(generics.ListAPIView):
    queryset = Invite.objects.all()
    serializer_class = InviteSerializer
    model = serializer_class.Meta.model
    paginate_by = 50
    permission_classes = [permissions.AllowAny,] 

class ListEventsView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    model = serializer_class.Meta.model
    paginate_by = 2
    permission_classes = [permissions.AllowAny,] 