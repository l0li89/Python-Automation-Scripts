import pandas as pd

table = pd.read_html("https://en.wikipedia.org/wiki/List_of_Game_of_the_Year_awards")
table[1].to_csv("GameList.csv")