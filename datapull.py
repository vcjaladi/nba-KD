from nba_py import player
from nba_py.player import get_player
import pandas as pd
from pprint import pprint


def gen_df_list(*playernames):
    players = []
    for i in playernames:
        first_last = i.split()
        players.append(get_player(first_last[0], first_last[-1]))

    player_stats = []
    for j in players:
        df_shot_list = pd.DataFrame()

        df_shot_list.append(player.PlayerShootingSplits(j).overall())

        playoffs = player.PlayerShootingSplits(j, season_type="Playoffs").overall()
        playoffs["Playoff"] = "Yes"
        df_shot_list.append(playoffs)

        df_shot_list["Name"] = i

        player_stats.append(df_shot_list)

    pd.concat(player_stats)


def gen_csv_files(path, df_list):
    for i in df_list:
        pass

if __name__ == "__main__":
    kd = get_player("Kevin", "Durant")
    pprint(player.PlayerSummary(kd).headline_stats()["PLAYER_NAME"][0])