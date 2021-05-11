from rest_framework import serializers
from .models import Messages, Userprofile


class MessageSerializer(serializers.ModelSerializer):

    sender_name = serializers.SlugRelatedField(many=False, slug_field='uid', queryset=Userprofile.objects.all())
    receiver_name = serializers.SlugRelatedField(many=False, slug_field='uid', queryset=Userprofile.objects.all())

    class Meta:
        model = Messages
        fields = ['sender_name', 'receiver_name', 'description', 'time']

