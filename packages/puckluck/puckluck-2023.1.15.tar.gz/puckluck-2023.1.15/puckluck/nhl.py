# imports
import requests
import pandas as pd


def extract_games(start="2022-10-01", end="2022-10-27"):
    """Uses the NHL stats api to get the games over the range of dates supplied

    Args:
        start (str, optional): Start date. Defaults to '2022-10-01'.
        end (str, optional): End Date. Defaults to '2022-10-27'.

    Returns:
        pd.DataFrame: DataFrame of the games over the window of start and end.
    """

    URL = "https://statsapi.web.nhl.com/api/v1/schedule"
    params = {"startDate": start, "endDate": end}
    resp = requests.get(URL, params=params)
    dates = resp.json()["dates"]
    game_data = []
    for date in dates:
        for game in date["games"]:
            parsed = pd.json_normalize(game)
            parsed.columns = parsed.columns.str.replace(".", "_", regex=True)
            parsed_dict = parsed.to_dict(orient="records")
            game_data.append(
                parsed_dict[0]
            )  # even though one game, records is a list of a single dict
    games = pd.DataFrame(game_data)
    return games


def extract_pbp(gid="2022020111"):
    """Get the PBP JSON for a single Game Id

    Args:
        gid (str, optional): The game id. Defaults to '2022020111'.

    Returns:
        dict: The PBP JSON as a dictionary
    """
    URL = f"http://statsapi.web.nhl.com/api/v1/game/{gid}/feed/live"
    resp = requests.get(URL)
    pbp = resp.json()
    return pbp


def transform_game_meta(pbp):
    """Cleanup the game metadata to return the info about the game contest

    Args:
    pbp (dict): The python dict for a singular game.

    Returns:
        pd.DataFrame: The parsed game data as a DataFrame

    """
    meta = pd.json_normalize(pbp.get("metaData"))
    meta["copyright"] = pbp.get("copyright")
    meta["gid"] = pbp.get("gamePk")
    meta["link"] = pbp.get("link")
    return meta


def transform_game_data(pbp):
    """Parse the information about a game include the info, teams in the contestx, and players

    Args:
        pbp (pd.DataFrame): A DataFrame that represents a dictionary, likely from nhl.extract_pbp

    Returns:
        tuple: A tuple of 3 dataframes game_info, teams and players
    """

    # get the game info
    game = pbp["gameData"]
    ginfo = pd.json_normalize(game.get("game"))
    ginfo.columns = "game_" + ginfo.columns
    gts = pd.json_normalize(game.get("datetime"))
    status = pd.json_normalize(game.get("status"))
    status.columns = "status_" + status.columns
    empty_venue = pd.DataFrame({"id": [None], "name": [None], "link": [None]})
    venue = pd.json_normalize(game.get("venue", empty_venue))
    venue.columns = "venue_" + venue.columns
    game_info = pd.concat([ginfo, gts, status, venue], axis=1)
    game_info = game_info.astype("object")  # everything as a string, parse later
    game_info.columns = game_info.columns.str.lower()
    # parse the teams from the game
    teams_d = game.get("teams")
    away = pd.json_normalize(teams_d.get("away"))
    home = pd.json_normalize(teams_d.get("home"))
    away.columns = away.columns.str.replace(".", "_").str.lower()
    home.columns = home.columns.str.replace(".", "_").str.lower()
    away["role"] = "away"
    home["role"] = "home"
    teams = pd.concat([away, home])
    teams["game_pk"] = game_info["game_pk"]
    # parse the players for the content
    players_d = game.get("players")
    pids = list(players_d.keys())
    players_list = [pd.json_normalize(players_d[x]) for x in pids]
    players = pd.concat(players_list)
    players.columns = players.columns.str.replace(".", "_").str.lower()
    players["game_pk"] = game_info["game_pk"]
    return (game_info, teams, players)


# def transform_livedata(pbp):
#     """Pull out the datasets from the livedata feed

#     Args:
#         pbp (dict): For a given gameId, likely the output of extract_pbp(gid)
#     """
#     livedata = pbp["liveData"]
#     box = livedata["boxscore"]
#     # parse refs
#     refs = pd.json_normalize(box["officials"])
#     refs.columns = refs.columns.str.replace(".", "_", regex=True)
#     # parse the team boxscore data
#     teams = box["teams"]
#     teams["away"].keys()
