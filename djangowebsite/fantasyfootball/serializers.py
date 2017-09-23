from rest_framework import serializers
from .models import Player
from .models import Team

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Player

        #all data return
        #fields = '__all__'

        #specific data return
        fields = ('name','user_team')



class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team

        fields = '__all__'