from django.db import models


class Team(models.Model):
    team_name = models.CharField(max_length=50)
    qb = models.CharField(max_length=50)
    rb = models.CharField(max_length=50)
    te = models.CharField(max_length=50)
    flex = models.CharField(max_length=50)
    defense = models.CharField(max_length=50)
    kicker = models.CharField(max_length=50)

    def __str__(self):
        return self.team_name



class Player(models.Model):
    name = models.CharField(max_length=75)
    nfl_team = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    user_team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name




