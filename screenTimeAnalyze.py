# Screen Time Analysis is the task of analyzing and creating a report on which applications and websites are used by the user for how much time.Apple devices have one of the best ways of creating a screen time report.
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import statsmodels.api as sm
data=pd.read_csv("Screentime-App-Details.csv")
print(data.head())
print(data.isnull().sum())
print(data.describe())
"""fig = px.bar(data_frame=data, x="Date", y="Times opened", color="App", title="Graph")
fig.show()"""
# fig
fig = px.bar(data_frame=data, x="Date", y="Usage", color="App", title="Usage Graph")
fig.show()
fig = px.bar(data_frame=data, x="Date", y="Notifications", color="App", title="Usage Graph")
fig.show()
fig = px.bar(data_frame=data, x="Date", y="Times opened", color="App", title="Graph")
fig.show()
fig=px.scatter( data_frame = data,  x="Notifications", y="Usage", size="Notifications", trendline="ols", title="Relationship Between Number of Notifications and Usage")
fig.show()