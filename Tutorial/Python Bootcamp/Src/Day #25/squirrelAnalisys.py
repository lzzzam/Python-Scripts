import os
import pandas as pd

DIR_NAME = os.path.dirname(__file__)
CSV_PATH = os.path.join(DIR_NAME, 'Squirrel_Data.csv')
OUT_PATH = os.path.join(DIR_NAME, "out.csv")
data = pd.read_csv(CSV_PATH)

colors = data["Highlight Fur Color"].unique()

dict = { "color" : [], "num" : []}

for color in colors:
    df  = data[ data["Highlight Fur Color"] == color]
    num = len( df["Highlight Fur Color"] )
    dict["color"].append(color)
    dict["num"].append(num)
    
out = pd.DataFrame(dict)

out.to_csv(OUT_PATH, index=False)
print(out)
    