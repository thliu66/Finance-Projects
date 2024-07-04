import requests
import pandas as pd
import ast
import plotly.express as px
import dash
from dash import Dash, html, dcc, Output, Input
import dash_mantine_components as dmc


def listing_ebitda(sector):
    df = requests.get('http://127.0.0.1:5000/EBITDA?Sector=' + sector).text
    df = ast.literal_eval(df)
    return df


named_sectors = ast.literal_eval(requests.get('http://127.0.0.1:5000/Sector').text)
EBITDA_by_sector = []
for sector in named_sectors:
    EBITDA_by_sector.append(sum(listing_ebitda(sector)))


df_EBITDA = pd.DataFrame(
    {
    'Sector': named_sectors,
    'EBITDA': EBITDA_by_sector
    }
)


dash._dash_renderer._set_react_version('18.2.0')
app = Dash(__name__)


app.layout = [
    dcc.Graph(id="graph"),
    html.Div(
        [
            dmc.MantineProvider(
                children = 
                [
                    dmc.MultiSelect(
                        data=named_sectors,
                        value=named_sectors,
                        description="Select the sectors that interest you.",
                        id="sectors-selected",
                        searchable=True,
                        w=400,
                        nothingFoundMessage="Nothing Found!",
                        
                    ),
                    dmc.Text(id="selected"),
                ]
            )
        ]
    )
]


@app.callback(
    Output("graph", "figure"), 
    Input("sectors-selected", "value"))
def generate_chart(value):
    df_filter = df_EBITDA.loc[df_EBITDA['Sector'].isin(value)]
    pie_chart = px.pie(df_filter, names = 'Sector', values='EBITDA', hole=.3)
    return pie_chart


if __name__ == "__main__":
    app.run(debug=True)
