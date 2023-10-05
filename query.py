from yfpy import Data
from yfpy.logger import get_logger
from yfpy.query import YahooFantasySportsQuery
from pathlib import Path
import json


# set directory location of private.json for authentication
auth_dir = Path(__file__).parent / "auth"

# set target directory for data output
data_dir = Path(__file__).parent / "output"

# create YFPY Data instance for saving/loading data
data = Data(data_dir)

key = None
secret = None
league_id = None
with open(Path(__file__).parent / f"auth/private.json") as f:
    d = json.load(f)
    key = d["consumer_key"]
    secret = d["consumer_secret"]
    league_id = d["league_id"]

# configure the Yahoo Fantasy Sports query
yahoo_query = YahooFantasySportsQuery(
    auth_dir,
    league_id,
    game_id=423,
    game_code="nfl",
    offline=False,
    all_output_as_json_str=False,
    consumer_key=key,
    consumer_secret=secret,
    browser_callback=True
)

# MY QUERIES

# for i in range(1, 5):
#     data.save(f"week_{i}_matchup", yahoo_query.get_league_matchups_by_week, {"chosen_week": i})
# data.save(f"week_5_matchup", yahoo_query.get_league_matchups_by_week, {"chosen_week": 5})
data.save("week_4_standings", yahoo_query.get_league_standings)