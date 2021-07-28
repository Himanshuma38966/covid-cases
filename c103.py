import pandas as pd
import plotly_express as px
#reading the csvfile
df = pd.read_csv("covid.csv")
#creating a line graph
fig = px.scatter(df,x="date",y="cases",color="country")
#to show the graph
fig.show()