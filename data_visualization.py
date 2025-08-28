
# Run this app with `python data_visualization.py`

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv("new_daily_sales.csv")


fig = px.line(df, x="date", y="sales")


app.layout = html.Div([
    html.H1('Pink Morsel Sales', id="header"),


    dcc.Graph(
        id='pink_morsel_graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)
