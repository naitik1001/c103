import pandas as pd
import plotly.express as px
df = pd.read_csv("C:/Users/gogof/Desktop/coding/hi-main/Copy+of+data+-+data (1).csv")
fig = px.scatter(df,x = 'date',y = 'cases',color = 'country')
fig.show()