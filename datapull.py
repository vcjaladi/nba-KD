# import statements
from nba_py import player
from nba_py.player import get_player
import pandas as pd
from os import makedirs, path


# function to generate a dictionary with various stat types for each entered player
def gen_dfs(*playernames):
    # create list with player objects using player names
    print("Starting...")
    players = []
    print("Generating players...")
    for name in playernames:
        first_last = name.split()
        players.append(get_player(first_last[0], first_last[-1]))

    print("Pulling Data from nba.stats.com...")
    # create dictionary with all data frames
    player_stats = dict()

    player_stats["Shooting Splits"] = shooting_splits(players)
    player_stats["Shot Types"] = shot_types(players)
    player_stats["Touch Time"] = touch_time(players)
    player_stats["Assisted Shots"] = assisted_shots(players)
    player_stats["Passes Made"] = passes_made(players)
    player_stats["Closest Defender"] = closest_defender(players)
    player_stats["Contested Rebounding"] = contested_rebounds(players)
    player_stats["Opponent Splits"] = opponent_splits(players)
    player_stats["Defensive Summary"] = defense_summ(players)
    player_stats["Assisted By"] = assisted_by(players)

    return player_stats


# pull general shooting splits
def shooting_splits(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerShootingSplits(each).overall()

        # add playoff shooting splits
        playoffs = player.PlayerShootingSplits(each, season_type="Playoffs").overall()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull general shooting splits
def shot_types(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerShootingSplits(each).shot_types_summary()

        # add playoff shooting splits
        playoffs = player.PlayerShootingSplits(each, season_type="Playoffs").shot_types_summary()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull assisted shots stats
def assisted_shots(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerShootingSplits(each).assisted_shots()

        # add playoff shooting splits
        playoffs = player.PlayerShootingSplits(each, season_type="Playoffs").assisted_shots()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull assisted shots stats broken down by the passer
def assisted_by(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerShootingSplits(each).assissted_by()

        # add playoff shooting splits
        playoffs = player.PlayerShootingSplits(each, season_type="Playoffs").assissted_by()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull shot stats by distance of closest defender
def closest_defender(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerShotTracking(each).closest_defender_shooting()

        # add playoff shooting splits
        playoffs = player.PlayerShotTracking(each, season_type="Playoffs").closest_defender_shooting()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull shot stats by touch time
def touch_time(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerShotTracking(each).touch_time_shooting()

        # add playoff shooting splits
        playoffs = player.PlayerShotTracking(each, season_type="Playoffs").touch_time_shooting()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull contested rebounding stats
def contested_rebounds(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerReboundTracking(each).num_contested_rebounding()

        # add playoff shooting splits
        playoffs = player.PlayerReboundTracking(each, season_type="Playoffs").num_contested_rebounding()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull stats for passes made
def passes_made(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerPassTracking(each).passes_made()

        # add playoff shooting splits
        playoffs = player.PlayerPassTracking(each, season_type="Playoffs").passes_made()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull opponent splits stats sorted by team
def opponent_splits(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerOpponentSplits(each).by_opponent()

        # add playoff shooting splits
        playoffs = player.PlayerOpponentSplits(each, season_type="Playoffs").by_opponent()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# pull defensive stat summary
def defense_summ(players):
    # gather and format shooting splits for all selected players
    all_player_list = []
    for each in players:
        # add regular season shooting splits to a new dataframe
        player_df = player.PlayerDefenseTracking(each).overall()

        # add playoff shooting splits
        playoffs = player.PlayerDefenseTracking(each, season_type="Playoffs").overall()
        playoffs["Playoff"] = "Yes"
        player_df = pd.concat([player_df, playoffs])

        # label the rows with the player name
        player_df["Name"] = player.PlayerSummary(each).headline_stats()["PLAYER_NAME"][0]

        # add the individual player's shooting splits to a list with all selected players' splits
        all_player_list.append(player_df)

    # concatenate all players' shooting splits together, generate an index num for each row, and make the index a column
    stats_df = pd.concat(all_player_list).reset_index(drop=True)
    stats_df["ID"] = stats_df.index

    return stats_df


# create CSVs for each data frame in a dictionary
def make_csv(df_dict):
    # create a folder for the CSVs
    makedirs(name="Player Stats", exist_ok=True)

    # make each CSV, name the file after the key
    for key in df_dict:
        df_dict[key].to_csv(path.join("Player Stats", key+r'.csv'))

if __name__ == "__main__":
    stats = gen_dfs("Kevin Durant", "Lebron James", "Stephen Curry")
    make_csv(stats)
