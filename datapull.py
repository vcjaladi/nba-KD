from nba_py import player
from nba_py.player import get_player
from pprint import pprint

kd = get_player("Kevin", "Durant")
lbj = get_player("Lebron", "James")

print(player.PlayerShotTracking(kd).closest_defender_shooting())
print(player.PlayerShotTracking(lbj).closest_defender_shooting())
