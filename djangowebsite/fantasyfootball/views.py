from django.shortcuts import render
from django.http import HttpResponse

from django.shortcuts import get_object_or_404
from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Team
from .models import Player
from .serializers import TeamSerializer
from .serializers import PlayerSerializer

def index(request):
    return HttpResponse("<h1> This is the player homepage </h1>")



#lists all teams or creates a new one
# team/
class TeamList(APIView):
    def get(self,request):
        teams = Team.objects.all()
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

    def post(self):
        pass