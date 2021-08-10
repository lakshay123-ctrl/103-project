import pandas as pd
import plotly.express as px

data = pd.read_csv("103data.csv")
datagraph = px.scatter(data,x = "date", y = "cases", color = "country",title = "103 class")
datagraph.show()