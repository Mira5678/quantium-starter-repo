# 1. Your task is to create a Dash app to visualise the data you generated in the last task. 
#    Lean on the resources linked below to learn more about the basics of working with Dash. 
#    Your application must incorporate the following elements:
#       1. A header which appropriately titles the visualiser
#       2. A line chart which visualises the sales data generated in the last task, sorted by date. Be sure to include appropriate axis labels for the chart.
 
# 2. Recall the original purpose of the Dash app you are building — 
# the goal is to answer Soul Foods’s question: “Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?” 

#To run this file type in "python task3.py"

from dash import Dash, html, dcc
import plotly.graph_objects as go
import pandas as pd

app = Dash()

new_daily_sales = pd.read_csv('new_daily_sales.csv')

df = pd.DataFrame(new_daily_sales)
df['date'] = pd.to_datetime(df['date'])
df['year'] = df['date'].dt.year

#Extract the years and the total sales of that year
yearly_sales = df.groupby('year')['sales'].sum().reset_index()


price_increase_date = '2021-01-15'
price_increase_dt = pd.to_datetime(price_increase_date)
price_increase_year = price_increase_dt.year


fig = go.Figure()

fig.add_trace(go.Scatter(
    x = yearly_sales['year'],
    y = yearly_sales['sales'],
    mode = 'lines',
    line = dict(color='blue')
))

fig.add_vline(
    x=price_increase_year,
    line_dash="dash",
    line_color="red",
    annotation_text="2021-01-15"
)

fig.update_layout(
    title='Pink Morsel Sales (year)',
    xaxis_title='Year',
    yaxis_title='Sales'
)

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel Sales (year)'),

    dcc.Graph(
        id='line-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
