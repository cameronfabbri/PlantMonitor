import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output

from datetime import datetime
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

f = open('../data/sensors.txt','r')
pos = 0

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div(
    html.Div([
        html.H1('Plant Monitor'),
        dcc.Graph(id='live-update-graph'),
        dcc.Interval(
            id='interval-component',
            interval=1*0000,
            n_intervals=0
        )
    ])
)

def getData(pos=0):
    f.seek(pos)
    if pos == 0:
        data = {
            'year': [],
            'month': [],
            'day': [],
            'hour': [],
            'minute': [],
            'temperature': [],
            'humidity': [],
            'light': [],
            'moisture': []
        }
    for line in f:
        line = line.rstrip().split(',')
        print 'line:',line
        exit()
        temperature = float(line[0])
        humidity = float(line[1])
        light = float(line[2])
        moisture = float(line[3])
        year = int(line[4])
        month = int(line[5])
        day = int(line[6])
        hour = int(line[7])
        minute = int(line[8])

        data['temperature'].append(temperature)
        data['humidity'].append(humidity)
        data['light'].append(light)
        data['moisture'].append(moisture)
        data['year'].append(year)
        data['month'].append(month)
        data['day'].append(day)
        data['hour'].append(hour)
        data['minute'].append(minute)

    pos = f.tell()
    return data, pos

@app.callback(Output('live-update-graph','figure'), [Input('interval-component','n_intervals')])
def update_metrics(n):

    try: pos
    except NameError: pos = 0

    data, pos = getData(pos)
    print 'pos:',pos

    fig = plotly.tools.make_subplots(rows=2,cols=1, vertical_spacing=0.2)

    fig['layout']['margin'] = {'l':30, 'r': 10, 'b': 30, 't': 10}
    fig['layout']['legend'] = {'x': 0, 'y': 1, 'xanchor': 'left'}

    fig.append_trace({'x':data['minute'], 'y':data['moisture']}, 1,1)

    return fig


if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
