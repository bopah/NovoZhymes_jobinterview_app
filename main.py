from dash import Dash, dcc, html, dash_table, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    # Title
    html.H1(children = "Explore the stats of the strongest or weakest Pokémon from each generation", style = {'fontSize': '40px', 'textAlign': 'center'}),
])



if __name__ == '__main__':
    app.run(debug=True)