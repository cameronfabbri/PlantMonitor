import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from datetime import datetime

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

available_indicators = ['All', 'Temperature', 'Humidity', 'Light', 'Moisture']

# Load the plant data
x = []
y = []

data = {}
with open('../data/sensors.txt', 'r') as f:
    for line in f:
        temperature = float(line.rstrip().split(',')[0])
        humidity = float(line.rstrip().split(',')[1])
        light = float(line.rstrip().split(',')[2])
        moisture = float(line.rstrip().split(',')[3])
        date = ','.join(line.rstrip().split(',')[4:])
        year = int(line.rstrip().split(',')[4])
        month = int(line.rstrip().split(',')[5])
        day = int(line.rstrip().split(',')[6])
        hour = int(line.rstrip().split(',')[7])
        minute = int(line.rstrip().split(',')[8])
        data['year'].append(year)
        data['month'].append(month)
        data['day'].append(day)
        data['hour'].append(hour)
        data['minute'].append(minute)
        data['date'].append(date)
        data['temperature'].append(temperature)
        data['humidity'].append(humidity)
        data['moisture'].append(moisture)

app.layout = html.Div([
    html.Div([

        html.Div([
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='Soil Moisture'
            ),
            dcc.RadioItems(
                id='xaxis-type',
                options=[{'label': i, 'value': i} for i in ['Linear', 'Log']],
                value='Linear',
                labelStyle={'display': 'inline-block'}
            )
        ],
        style={'width': '100%', 'display': 'inline-block'}),

    ]),

    dcc.Graph(id='indicator-graphic'),

    dcc.Slider(
        id='time--slider',
        min=data['day'].min(),
        max=data['day'].max(),
        value=data['day'].max(),
        marks={str(day): str(day) for day in df['day'].unique()}
    )
])

@app.callback(
    dash.dependencies.Output('indicator-graphic', 'figure'),
    [dash.dependencies.Input('xaxis-column', 'value'),
     dash.dependencies.Input('yaxis-column', 'value'),
     dash.dependencies.Input('xaxis-type', 'value'),
     dash.dependencies.Input('yaxis-type', 'value'),
     dash.dependencies.Input('year--slider', 'value')])
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df['Year'] == year_value]

    return {
        'data': [go.Scatter(
            x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
            y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
            text=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'],
            mode='markers',
            marker={
                'size': 15,
                'opacity': 0.5,
                'line': {'width': 0.5, 'color': 'white'}
            }
        )],
        'layout': go.Layout(
            xaxis={
                'title': xaxis_column_name,
                'type': 'linear' if xaxis_type == 'Linear' else 'log'
            },
            yaxis={
                'title': yaxis_column_name,
                'type': 'linear' if yaxis_type == 'Linear' else 'log'
            },
            margin={'l': 40, 'b': 40, 't': 10, 'r': 0},
            hovermode='closest'
        )
    }


if __name__ == '__main__':
    app.run_server(debug=True)
