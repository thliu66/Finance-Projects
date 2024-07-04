import dash
import dash_mantine_components as dmc
from dash import html

dash._dash_renderer._set_react_version('18.2.0')
app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dmc.MantineProvider(
            children=[
                dmc.MultiSelect(
                    data=[
                        {
                            "group": "Frontend",
                            "items": [
                                {"value": "React", "label": "React"},
                                {"value": "Angular", "label": "Angular"},
                            ],
                        },
                        {
                            "group": "Backend",
                            "items": [
                                {"value": "Svelte", "label": "Svelte"},
                                {"value": "Vue", "label": "Vue"},
                            ],
                        },
                    ],
                    w=400,
                )
            ]
        )
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)