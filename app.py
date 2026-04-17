from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash()

df = pd.read_csv(
    "data/output.csv",
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
    html.H1(children='Sales of each region per day'),

    html.Div(children='''
    This graph shows the sales of each region per day for the product "pink morsel".
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run(debug=True)