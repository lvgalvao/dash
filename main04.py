from dash import Dash
from dash_html_components import Div, H1, P, H3
from dash_core_components import Graph, Dropdown, Slider, Checklist
from dash.dependencies import Input, Output
from random import randint


app = Dash(__name__)


N = 20

database = {
    "index": list(range(N)),
    "femsa": [randint(1, 1000) for _ in range(N)],
    "andina": [randint(1, 1000) for _ in range(N)],
    "arca": [randint(1, 1000) for _ in range(N)],
}


app.layout = Div(
    children=[
        H1("ICE Score"),
        H3("Valor ICE Score por engarrafadora ao longo das coletas"),
        Checklist(
            id="meu_check_list",
            options=[
                {"label": "Femsa", "value": "femsa"},
                {"label": "Andina", "value": "andina"},
                {"label": "Arca", "value": "arca"},
            ],
            value=["femsa"],
        ),
        Graph(
            id="meu_grafico",
            config={"displayModeBar": False},
        ),
        Dropdown(
            id="meu_dropdown",
            options=[
                {"label": "Linha", "value": "line"},
                {"label": "Barra", "value": "bar"},
            ],
            value="line",
        ),
    ]
)


@app.callback(
    Output("meu_grafico", "figure"),
    [
        Input("meu_check_list", "value"),
        Input("meu_dropdown", "value"),
    ],
)
def my_callback(input_data, graph_type):
    grafico = {"data": []}
    for x in input_data:
        grafico["data"].append(
            {"y": database[x], "x": database["index"], "name": x, "type": graph_type},
        )
    return grafico


app.run_server(debug=True)
