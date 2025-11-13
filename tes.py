import pandas as pd

dfTrainVal = pd.read_json("static/data/trainvalloss.json")

print(dfTrainVal.to_dict(orient="records"))