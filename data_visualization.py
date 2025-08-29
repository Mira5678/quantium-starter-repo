
# Run this app with `python data_visualization.py`

from dash import Dash, html, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd


app = Dash()


df = pd.read_csv("new_daily_sales.csv")


fig = px.line(df, x="date", y="sales")


app.layout = html.Div([

    #header
    html.H1('Pink Morsel Sales', id="header", style={'text-align':'center', 'font-family':'"Courier New", monospace', 'font-size':'32px'}),

    #radio button
    dcc.RadioItems(
        [
            {
                "label": html.Div(['All'], style={'color': '#DE73C3', 'display':'inline-block'}),
                "value": "All",
            },

            {
                "label": html.Div(df['region'].unique()[0], style={'color': '#00DB52', 'display':'inline-block'}),
                "value": "north",
            },

            {
                "label": html.Div(df['region'].unique()[1], style={'color': '#DC481C', 'display':'inline-block'}),
                "value": "south",
            },

            {
                "label": html.Div(df['region'].unique()[2], style={'color': '#4E83D9', 'display':'inline-block'}),
                "value": "east",
            },

            {
                "label": html.Div(df['region'].unique()[3], style={'color': '#DBCC3B', 'display':'inline-block'}),
                "value": "west",
            },

        ],
        inputStyle={'margin-right': '0.375rem',
                    'transform':'scale(1.5)',
                    'cursor':'pointer'},
        labelStyle={'font-size': '15px', 
                    'font-family': '"Courier New", monospace',
                    'padding': '0.313rem 1rem',
                    'margin': '0.625rem',
                    'border': '2px solid #2A5FDB',
                    'border-radius': '10px'},
        style={
        'text-align': 'center',
        'width': '100%'
        },
        value = "All",
        id='region_choice',
        inline=True
    ),

    #visualization
    dcc.Graph(
        id='line_graph',
        figure=fig
    ),
])

@callback(
    Output('line_graph', 'figure'),
    Input('region_choice', 'value')
)

def update_visualization(selected_region):

    dff = df.copy()

    if selected_region != 'All':
        dff = dff[dff['region'] == selected_region]

    fig = px.line(dff, x='date', y='sales')

    return fig


if __name__ == '__main__':
    app.run(debug=True)
