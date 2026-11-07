import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('SpaceX Launch Records Dashboard', style={'textAlign': 'center'}),
    dcc.Dropdown(id='site-dropdown', options=[{'label': 'All Sites', 'value': 'ALL'}]),
    html.Div(dcc.Graph(id='success-pie-chart')),
    dcc.RangeSlider(id='payload-slider', min=0, max=10000, step=1000, value=[0, 10000]),
    html.Div(dcc.Graph(id='success-payload-scatter-chart')),
])

if __name__ == '__main__':
    app.run_server()
