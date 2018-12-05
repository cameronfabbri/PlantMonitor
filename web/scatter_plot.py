import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from datetime import datetime
from scipy import signal
import numpy as np

#def denormalize(x,a,b):

def normalize(x,a,b):
    return (b-a)*((x-np.min(x))/(np.max(x)-np.min(x)))+a

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('../data/sensors.csv')

dates = [datetime.strptime(x,'%Y-%m-%d-%H-%M-%S') for x in df['date']]

# Take a random 25% of the data
idx = np.random.choice(np.arange(len(dates)), int(len(dates)/4), replace=False)

moisture = df['moisture'].values
temperature = df['temperature'].values
humidity = df['humidity'].values
light = df['light'].values

# Put readings into a common range (basically percentage)
moisture = normalize(moisture,0,100)[idx]
temperature = normalize(temperature,0,100)[idx]
humidity = normalize(humidity,0,100)[idx]
light = normalize(light,0,100)[idx]

app.layout = html.Div([
    html.H1('Plant Monitor'),
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                go.Scatter(
                    x = dates,
                    y = signal.savgol_filter(moisture,101,3),
                    mode='markers',
                    opacity=0.9,
                    marker={
                        'size': 8,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='Moisture'
                ),
                go.Scatter(
                    x = dates,
                    y = signal.savgol_filter(temperature,101,3),
                    mode='markers',
                    opacity=0.9,
                    marker={
                        'size': 8,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='Temperature'
                ),
                go.Scatter(
                    x = dates,
                    y = signal.savgol_filter(humidity,101,3),
                    mode='markers',
                    opacity=0.9,
                    marker={
                        'size': 8,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='Humidity'
                ),
                go.Scatter(
                    x = dates,
                    y = signal.savgol_filter(light,101,3),
                    mode='markers',
                    opacity=0.9,
                    marker={
                        'size': 8,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name='Light'
                )

            ],
            'layout': go.Layout(
                xaxis={'type': 'date', 'title': 'Date'},
                yaxis={'title': 'Sensor Readings'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0',debug=True)
