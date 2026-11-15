import pandas as pd

GAMES_URL = "https://raw.githubusercontent.com/nflverse/nfldata/master/data/games.csv"

games = pd.read_csv( GAMES_URL,
                       index_col = 0)

col = games.home_coach.describe()

print(col)