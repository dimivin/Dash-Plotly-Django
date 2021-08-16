import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import requests
from dash.dependencies import Input, Output
from django_plotly_dash import DjangoDash

btc_hourly = "https://www.vinterapi.com/api/v2/single_assets_hourly/?symbol=btc-usd-p-h"
eth_hourly = "https://www.vinterapi.com/api/v2/single_assets_hourly/?symbol=eth-eu-p-h"

url = btc_hourly

vinter_key = "Fzwtx07C.vkwN5zYY8UDE7hdgX97TLfhoiRWziFhD"

headers = {"Authorization": vinter_key}

app = DjangoDash("SimpleExample")


app.layout = html.Div([
    dcc.Interval(
                id='my_interval',
                n_intervals=0,       # number of times the interval was activated
                interval=120*1000,   # update every 2 minutes
    ),
    dcc.Graph(id="VinterGraph"),   # empty graph to be populated by line chart
])

#-------------------------------------------------------------------------------
@app.callback(
    Output(component_id='VinterGraph', component_property='figure'),
    [Input(component_id='my_interval', component_property='n_intervals')]
)
def update_graph(n):
    """Pull financial data from Alpha Vantage and update graph every 2 minutes"""

    params = {"limit": "100"}

    r= requests.get(url, headers=headers, params=params)

    d = r.json()
    data = d

    df = pd.DataFrame(d['data'])

    line_chart = px.line(
                    data_frame=df,
                    x='datetime',
                    y='value',
                    # color='indicator',
                    title="BTC"
                    # title="Stock: {}".format(ttm_meta_data['2. Symbol'])
                 )
    return (line_chart)
