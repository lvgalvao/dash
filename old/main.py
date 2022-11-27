from dash import Dash
from dash_html_components import H1, Div, P, H2
from dash_core_components import Graph
from random import randint

N = 20

database = {"index": list(range(N)), "maiores": [randint(1, 1000) for _ in range(N)]}

external_stylesheets = ["https://unpkg.com/terminal.css@0.7.1/dist/terminal.min.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = Div(
    children=[
        H1("Boas vindas"),
        P("Esse é o nosso layout de gráfico"),
        H2("Peso"),
        P("A seguir gráfico de peso"),
        H2("Altura"),
        P("A seguir gráfico de Altura"),
        Graph(
            figure={
                "data": [
                    {"y": [1, 2, 3, 4], "type": "box"},
                    {"y": [1, 2, 3, 4], "type": "box"},
                ],
                "layout": {},
            }
        ),
        Graph(
            figure={
                "data": [
                    {"y": [1, 2, 3, 4], "type": "box"},
                    {"y": [1, 2, 3, 4], "type": "box"},
                ],
                "layout": {},
            }
        ),
        Graph(
            figure={
                "data": [
                    {"x": [1, 2, 3, 4], "y": [1, 2, 3, 4], "type": "line", "name": "a"},
                    {"x": [1, 2, 3, 4], "y": [4, 3, 2, 1], "type": "line", "name": "b"},
                    {
                        "x": [1, 2, 3, 4],
                        "y": [5, 5, 5, 5],
                        "type": "bar",
                        "name": "sum",
                    },
                ],
                "layout": {},
            }
        ),
        Graph(
            config={"displayModeBar": False},
            figure={
                "data": [
                    {
                        "values": [33, 16, 50],
                        "labels": ["a", "b", "c"],
                        "type": "pie",
                    },
                ],
                "layout": {
                    "title": "minha pizza",
                    "paper_bgcolor": "#222225",
                    "titlefont": {
                        "size": 30,
                        "color": "#e8e9ed",
                    },
                },
            },
        ),
        Graph(
            config={"displayModeBar": False},
            figure={
                "data": [
                    {
                        "y": database["maiores"],
                        "x": database["index"],
                        "name": "maiores",
                    },
                ],
                "layout": {
                    "title": "minha barra",
                },
            },
        ),
    ]
)

app.run_server()
