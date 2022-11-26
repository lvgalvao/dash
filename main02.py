from dash import Dash
from dash_html_components import Div, H1, H3
from dash_core_components import Graph, Dropdown, Slider, Checklist
from random import randint


app = Dash(__name__)


N = 20

database = {
    "index": list(range(N)),
    "maiores": [randint(1, 1000) for _ in range(N)],
    "menores": [randint(1, 1000) for _ in range(N)],
    "bebes": [randint(1, 1000) for _ in range(N)],
}


app.layout = Div(
    children=[
        H1("Evento X"),
        H3("idade das pessoas que foram ao evento"),
        Dropdown(
            options=[
                {"label": "Menores de Idade", "value": "menores"},
                {"label": "Bebes", "value": "bebes"},
                {"label": "Maiores de idade", "value": "maiores"},
            ],
            value="menores",
        ),
        Slider(min=0, max=10, step=1, value=5),
        Graph(
            config={"displayModeBar": False},
            figure={
                "data": [
                    {
                        "y": database["maiores"],
                        "x": database["index"],
                        "name": "Maiores",
                    },
                ],
            },
        ),
        Checklist(
            options=[
                {"label": "Menores de Idade", "value": "menores"},
                {"label": "Bebes", "value": "bebes"},
                {"label": "Maiores de idade", "value": "maiores"},
            ],
            value=["bebes"],
        ),
    ]
)


app.run_server(debug=True)
