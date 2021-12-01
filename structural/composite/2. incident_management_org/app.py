from team import Team
from truck import Truck
from hr import HR

sub_team1 = Team()
truck_kun1 = Truck()
hr1 = HR()
hr2 = HR()
sub_team1.add(truck_kun1)
sub_team1.add(hr1)
sub_team1.add(hr2)

sub_team2 = Team()
truck_kun2 = Truck()
hr3 = HR()
hr4 = HR()
sub_team2.add(truck_kun2)
sub_team2.add(hr3)
sub_team2.add(hr4)

team = Team()
team.add(sub_team1)
team.add(sub_team2)
team.action_when_fire_occure()