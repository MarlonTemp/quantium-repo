from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
from pathlib import Path

app = Dash()

BASE_DIR = Path(__file__).resolve().parent

df = pd.read_csv(
    BASE_DIR / "data" / "output.csv",
    header=None,
    names=["sales", "date", "region"],
)
df["sales"] = df["sales"].str.replace("$", "", regex=False).astype(float)
df["date"] = pd.to_datetime(df["date"])

fig = px.line(
    df,
    x="date",
    y="sales",
    color="region",
    title="Sales by region",
)

app.layout = html.Div(children=[
    html.H1(id="header", children='Sales of each region per day'),

    html.Div(children='''
    This graph shows the sales of each region per day for the product "pink morsel".
    '''),

    html.Form([
        html.Label("Select a region:"),
        dcc.RadioItems(
            id="region_picker",
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'South', 'value': 'south'},
                {'label': 'East', 'value': 'east'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All regions', 'value': 'all'},
            ],
            value='all'
        )
    ]),

    dcc.Graph(
        id='visualisation',
        figure=fig
    )
])


@app.callback(
    Output('visualisation', 'figure'),
    Input('region_picker', 'value'))
def update_graph(selected_region):
    chart_data = df if selected_region == 'all' else df[df['region'] == selected_region]
    title = 'Sales by region' if selected_region == 'all' else f"Sales in {selected_region.title()}"

    return px.line(
        chart_data,
        x='date',
        y='sales',
        color='region',
        title=title,
    )

if __name__ == '__main__':
    app.run(debug=True)