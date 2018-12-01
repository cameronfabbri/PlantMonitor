import dash
import dash_core_components as dcc
import dash_html_components as html
import matplotlib
matplotlib.use('Pdf')
import matplotlib.pyplot as plt
from datetime import datetime
import matplotlib.dates as plt_dates
from matplotlib.pyplot import figure
import time

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

'''
data = {}
with open('../../data/sensors.txt', 'r') as f:
    for line in f:
        temperature = float(line.rstrip().split(',')[0])
        humidity = float(line.rstrip().split(',')[1])
        light = float(line.rstrip().split(',')[2])
        moisture = float(line.rstrip().split(',')[3])
        data[','.join(line.rstrip().split(',')[4:])] = [temperature, humidity, light, moisture]
'''

def follow(f,idx):
    f.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        sensor_reading = line.rstrip().split(',')[4:]
        print(sensor_reading)
        exit()
        x.append(idx)
        y1.append(sensor_reading[0])
        y2.append(sensor_reading[1])
        y3.append(sensor_reading[2])
        y4.append(sensor_reading[3])
        yield line

'''
i = 0
x = []
y1 = []
y2 = []
y3 = []
y4 = []
for date, sensor_reading in data.iteritems():
    date = datetime.strptime(date, '%Y,%m,%d,%H,%M,%S')
    date = plt_dates.date2num(date)
    x.append(i)
    y1.append(sensor_reading[0])
    y2.append(sensor_reading[1])
    y3.append(sensor_reading[2])
    y4.append(sensor_reading[3])
    i += 1
'''
app.layout = html.Div(children=[
    html.H1(children='Plant Monitor'),

    html.Div(children='''
        Monitoring my plant via python
    '''),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': x, 'y': y1, 'type': 'line', 'name': 'Temperature'},
                {'x': x, 'y': y2, 'type': 'line', 'name': 'Humidity'},
                {'x': x, 'y': y3, 'type': 'line', 'name': 'Light'},
                {'x': x, 'y': y4, 'type': 'line', 'name': 'Moisture'}
            ],
            'layout': {
                'title': 'Plant Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    f = '../../data/sensors.txt'
    loglines = follow(f)
    app.run_server(host='0.0.0.0', debug=True)
