import dash
from dash import Dash, dcc, html
import numpy as np
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input,Output
import plotly.express as px
from plotly.graph_objs import Layout

external_stylesheet = [
    {
      "href":"https://cdn.jsdelivr.net/npm/bootstrap@5.3.9/dist/css/bootstrap.min.css",
      "rel":"stylesheet",
      "integrity":"sha384-yEPZ7jP9S0QKiUQ0m3jjsO4ProIW7wvR9gXkI7JOGa2XVsw53Yke2bsdkBbjmmiX",
      "crossorigin":"anonymous"
   }
]
patints = pd.read_csv('covid_demo_2000_state_last.csv')
total=patints.shape[0]
Active=patints[patints['Status']=='Confirmed'].shape[0]
Recovered=patints[patints['Status']=='Recovered'].shape[0]
Deceased=patints[patints['Status']=='Deceased'].shape[0]

options=[
    {'label':"All",'value':"all"},
    {'label':"Hospitalized",'value':"Hospitalized"},
    {'label':"Recovered",'value':"Recovered"},
    {'label':"Deceased",'value':"Deceased"},
]

options1=[
    {'label': "All", 'value': "all"},
    {'label': "Mask", 'value': "Mask"},
    {'label': "Sanitizer", 'value': "Sanitizer"},
     {'label': "Oxygen", 'value': "Oxygen"}
]
options2=[
    {'label': "All", 'value': "Status"},
    {'label': "Red Zone", 'value': "Red Zone"},
    {'label': "Blue Zone", 'value': "Blue Zone"},
    {'label': "Green Zone", 'value': "Green Zone"},
    {'label': "Orange Zone", 'value': "Orange Zone"}


]

app = dash.Dash(__name__,external_stylesheets=external_stylesheet)

server = app.server

app.layout = html.Div([
    html.H1("Corona Virus Pandemic"),
    html.Div([
        html.Div([

            # Total case card
            html.Div([
                html.Div([
                    html.H3("Total Case",className="text-light"),
                    html.H4(total,className="text-light"),
                ],className="card-body")
            ],className="card bg-success"),
        ],className="col-md-3"),

        # Total case card
        html.Div([
            html.Div([
                html.Div([
                    # Total Active case
                    html.H3("Active Cases", className="text-light"),
                    html.H4(Active, className="text-light"),
                ], className="card-body")
            ], className="card bg-info"),
        ],className="col-md-3"),

        # Total Recovered Case
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Recovered Case", className="text-light"),
                    html.H4(Recovered, className="text-light"),
                ], className="card-body")
            ], className="card bg-warning"),
        ],className="col-md-3"),

        # Total Death Case
        html.Div([
            html.Div([
                html.Div([
                    html.H3("Total Death", className="text-light"),
                    html.H4(Deceased, className="text-light"),
                ], className="card-body")
            ], className="card bg-danger"),
        ],className="col-md-3"),
    ],className="row"),

# Pychart and Middle Part

    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='plot-graph',options=options1,value='all'),
                    dcc.Graph(id='graph'),
                ],className="card-body"),
            ],className="card"),
        ],className="col-md-6"),
        # Paychart
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='my_dropdown',options=options2,value='Status'),
                    dcc.Graph(id='the_graph'),
                ],className='card-body'),
            ],className='card'),
        ],className="col-md-6"),
    ],className="row"),


    #Graph Page
    html.Div([
        html.Div([
            html.Div([
                html.Div([
                    dcc.Dropdown(id='picker',options=options,value='all'),
                    dcc.Graph(id='bar'),
                ],className="card-body"),
            ],className="card"),
        ],className="col-md-12"),
    ],className="row"),
],className="container")



@app.callback(Output('bar',"figure"),[Input('picker','value')])
def update_graph(type):
    if type =='all':
        return{"data":[go.Bar(x=patints['State'],y=patints["Total"])],
               'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}

    if type =='Hospitalized':
        return{"data":[go.Bar(x=patints['State'],y=patints["Hospitalized"])],
               'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}

    if type =='Recovered':
        return{"data":[go.Bar(x=patints['State'],y=patints["Recovered"])],
               'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}

    if type =='Deceased':
        return{"data":[go.Bar(x=patints['State'],y=patints["Deceased"])],
               'layout':go.Layout(title="State Total Count",plot_bgcolor='orange')}



@app.callback(Output('graph','figure'),[Input('plot-graph','value')])
def generater_graph(type):
    if type == 'all':
        counts = patints.groupby('Status')['Total'].sum()
        return {"data": [go.Bar(x=counts.index, y=counts.values)],
                "layout": go.Layout(title="All Commodities Total Count", plot_bgcolor='pink')}
    if type == 'Mask':
        counts = patints.groupby('Status')['Mask'].sum()
        return {"data": [go.Bar(x=counts.index, y=counts.values)],
                "layout": go.Layout(title="Mask Total Count", plot_bgcolor='pink')}
    if type == 'Sanitizer':
        counts = patints.groupby('Status')['Sanitizer'].sum()
        return {"data": [go.Bar(x=counts.index, y=counts.values)],
                "layout": go.Layout(title="Sanitizer Total Count", plot_bgcolor='pink')}
    if type == 'Oxygen':
        counts = patints.groupby('Status')['Oxygen'].sum()
        return {"data": [go.Bar(x=counts.index, y=counts.values)],
                "layout": go.Layout(title="Oxygen Total Count", plot_bgcolor='pink')}


@app.callback(Output('the_graph',"figure"),[Input('my_dropdown','value')])
def generate_graph(my_dropdown):
    piechart=px.pie(data_frame=patints,names=my_dropdown,hole=0.3)
    return (piechart)

#Provide Local Host using Flask
if __name__ == '__main__':
    app.run(debug=True)
