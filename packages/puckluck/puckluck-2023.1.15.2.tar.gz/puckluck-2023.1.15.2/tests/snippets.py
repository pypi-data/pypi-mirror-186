# clearly not tests, but just get off the ground
from puckluck.nhl import extract_games, extract_pbp
from puckluck.nhl import transform_game_data
import pandas as pd
import warnings

# filter future warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


g = extract_games()
gid = g.gamePk.sample(1).tolist()[0]
pbp = extract_pbp(gid)
# gdata = pbp.get("gameData")

# the transformed game data
ginfo, teams, players = transform_game_data(pbp)
