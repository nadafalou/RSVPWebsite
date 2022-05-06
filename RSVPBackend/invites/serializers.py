from operator import inv
from rest_framework import serializers
from invites.models import Invite, Event
from django.db.models import Sum

class InviteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invite
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    invites = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    # print(type(invites))
    confirmedNum = serializers.IntegerField(source='total_confirmed')
    
    class Meta:
        model = Event
        fields = ('name', 'datetime', 'invites', 'confirmedNum')
        extra_kwargs = {
            'name': {'required': True}, 
            'datetime': {'required': True}, 
            'invites': {'required': False}, 
        }


class CreateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ('name', 'datetime')


class CreateInviteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invite
        fields = ['event', 'names', 'invitedNum']
        extra_kwargs = {
            'names': {'required': True}, 
            'invitedNum': {'required': True}, 
            'event': {'required': True}, 
        }

    def create(self, validated_data):
        return Invite.objects.create(
            names=validated_data['names'],
            invitedNum=validated_data['invitedNum'],
            event=validated_data['event']
        )

class UpdateInviteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Invite
        fields = ['replied', 'requestedSong', 'confirmedNum', 'allergies']
    