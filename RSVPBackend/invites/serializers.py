from rest_framework import serializers
from invites.models import Invite, Event

class InviteSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Invite
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = '__all__'


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
    