#!/bin/python
import random
from datetime import datetime
import plotly.graph_objects as go
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input

DATASET_PATH = "custom_dataset.csv"

# initialialize app ###########################################################
app3 = dash.Dash(__name__)
server = app3.server

app3.layout = html.Div([
    html.Div([
        html.H1(
            children="LIVE DASHBOARD EXAMPLE",
        )
    ], className='container'),
    html.Div([
        html.Div([
            dcc.Graph(id='fig_3'),
            dcc.Interval(id='fig_3_update', interval=1*1000, n_intervals=0)
        ], className='container'),
    ], className='row'),
    html.Div([
        html.Div([
            html.A('footer', href='#')
        ], className='container',
                 id='footer')
    ], className='row')
], className='container-fluid')


# updating and generating the figures #########################################
@app3.callback([Output('fig_3', 'figure')],
               [Input('fig_3_update', 'n_intervals')])
def update_data(_):
    """ Update/Generate the Figures """
    ts_cases = pd.read_csv(DATASET_PATH, parse_dates=['timestamp'])
    ts_cases = ts_cases[['timestamp', 'voltage']]

    # generate fake current numbers
    current_date = datetime.now()
    c_cases = random.random()

    # function to update the csv files with current number
    def update_time_series(file, label, current_value, csvfile, current_date):
        last_date = csvfile['timestamp'].dt.date.max()
        if last_date == current_date:
            if int(csvfile[csvfile.timestamp.dt.date
                           == last_date][label].values) != current_value:
                csvfile.loc[csvfile['timestamp']
                            == last_date, label] = current_value
        else:
            csvfile = csvfile.append({
                'timestamp': current_date,
                label: current_value
            }, ignore_index=True)
        csvfile.to_csv(file)

    # updating the csv file
    update_time_series(
        DATASET_PATH,
        label='voltage',
        current_value=c_cases,
        csvfile=ts_cases,
        current_date=current_date
    )

    # creating fig 3 ##########################################################
    fig_3 = go.Figure(
        data=go.Scatter(
            x=ts_cases['timestamp'],
            y=ts_cases['voltage'],
            mode='lines',
            name='voltage'
        )
    )
    fig_3.update_layout(
        title='RMS VOLTAGE',
        legend_orientation='h',
        legend=dict(x=0.1, y=-0.05))
    fig_3.update_xaxes(showgrid=False, zeroline=False, showline=False)
    fig_3.update_yaxes(showgrid=False, zeroline=False, showline=False)

    return [fig_3]


if __name__ == '__main__':
    app3.run_server(debug=True)
