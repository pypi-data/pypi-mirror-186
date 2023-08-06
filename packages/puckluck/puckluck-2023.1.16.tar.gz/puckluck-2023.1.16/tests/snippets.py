# clearly not tests, but just get off the ground
from puckluck.nhl import extract_games, extract_pbp
from puckluck.nhl import transform_game_data, transform_game_meta
from puckluck.nhl import transform_official, transform_plays
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

# game api metadata
meta = transform_game_meta(pbp)

# get the official data
refs, decision = transform_official(pbp)

# parse the plays
cur, period, penalty, scoring, ppf_df, pbp_df = transform_plays(pbp)
