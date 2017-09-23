from django.contrib import admin
from .models import Player
from .models import Team


#allows access to player,team db
admin.site.register(Player)
admin.site.register(Team)