# clearly not tests, but just get off the ground
from puckluck import nhl
import pandas as pd
import warnings

# filter future warnings
warnings.simplefilter(action="ignore", category=FutureWarning)


g = nhl.extract_games()
gid = g.gamePk.sample(1).tolist()[0]
pbp = nhl.extract_pbp(gid)
# gdata = pbp.get("gameData")

# the transformed game data
ginfo, teams, players = nhl.extract_game_data(pbp)

# game api metadata
meta = nhl.extract_game_meta(pbp)

# get the official data
refs, decision = nhl.extract_official(pbp)

# parse the plays
cur, period, penalty, scoring, ppf_df, pbp_df = nhl.extract_plays(pbp)
