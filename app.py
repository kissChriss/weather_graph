import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv
import pandas as pd


app = dash.Dash()
app.config.supress_callback_exceptions = True

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
          'August', 'September', 'October', 'November', 'December']

days = (range(1, 32))

def _create_app():
    app.layout = html.Div([
        html.Div([
            html.Div([
                html.H1('Weather live graphs', style={'textAlign': 'center'}),
                html.P(html.I('Saint-Petersburg weather statistic for 16 years'), style={'textAlign': 'center', 'color':'grey'}),
            ], style={'backgroundColor': '#fff',  'box-shadow': '0px 0px 7px -4px #000'}),
            dcc.Dropdown(
                id='month-dropdown',
                options=[{'label': i, 'value': i} for i in months],
                value='January', clearable=False),
            dcc.Dropdown(
                id='day-dropdown',
                options=[{'label': i, 'value': i} for i in days],
                value='24', clearable=False),
            html.Br(),
            html.Div([
                dcc.Graph(
                    id='grapher', config={'displayModeBar': False}, style={'width': '100%',  'box-shadow': '0px 0px 7px -4px #000'})
                ]),
            html.Br(),
        ], style={'width': '70%', 'margin': '0px auto',})
    ], style={'backgroundColor': '#fff'})
    return app

@app.callback(Output('grapher', 'figure'),
              [Input('month-dropdown', 'value'),
               Input('day-dropdown', 'value')])
def search_data(month_dropdown, day_dropdown):
    filename = 'Months/' + month_dropdown + '.csv'
    with open(filename, 'r', newline='') as file:
        day_array = []
        for row in csv.reader(file):
            day_array.append(row)
        day = int(day_dropdown)
        day_per_year = day_array[day]
    years = (range(2000, 2017))
    row = list(zip(years, day_per_year))
    header = ('date', 't')
    new_file = 'new.csv'
    with open(new_file, 'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for item in row:
            writer.writerow(item)
    new_file = pd.read_csv('new.csv')
    return {
        'data': [{
            'x': new_file['date'],
            'y': new_file['t']
        }], 'layout': {'margin': {'l': 40, 'r': 20, 't': 20, 'b': 30}}
    }

app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

if __name__ == '__main__':
    app = _create_app()
    app.run_server()