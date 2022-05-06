from rest_framework import serializers
from invites.models import Guest

class GuestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guest
        fields = '__all__'

class CreateGuestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Guest
        fields = ['names', 'invitedNum']
        extra_kwargs = {
            'names': {'required': True}, 
            'invitedNum': {'required': True}, 
        }

    def create(self, validated_data):
        return Guest.objects.create(
            names=validated_data['names'],
            invitedNum=validated_data['invitedNum']
        )

class UpdateGuestSerializer(serializers.ModelSerializer):

    class Meta:
        model = Guest
        fields = ['replied', 'requestedSong', 'confirmedNum', 'allergies']
    