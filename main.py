from dash import Dash, dcc, html, dash_table, Input, Output

app = Dash(__name__)

app.layout = html.Div([
    # Title
    html.H1(children = "Explore the stats of the strongest or weakest Pokémon from each generation", style = {'fontSize': '40px', 'textAlign': 'center'}),

    # Wrapping the two dropdowns and stats+image+graph together, so I can place them side by side
    html.Div(children = [
        # Wrapping the two dropdowns together
        html.Div(children = [
            html.Label("Choose a Generation"),
            dcc.Dropdown(id = 'Gen_dropdown',
                        options = [
                            {'label': 'Generation 1', 'value': 'Generation 1'},
                            {'label': 'Generation 2', 'value': 'Generation 2'},
                            {'label': 'Generation 3', 'value': 'Generation 3'},
                            {'label': 'Generation 4', 'value': 'Generation 4'},
                            {'label': 'Generation 5', 'value': 'Generation 5'},
                            {'label': 'Generation 6', 'value': 'Generation 6'},
                            {'label': 'Generation 7', 'value': 'Generation 7'},
                            {'label': 'Generation 8', 'value': 'Generation 8'},
                            {'label': 'Generation 9', 'value': 'Generation 9'},
                            {'label': 'All Time', 'value': 'All Time'},
                        ],
                        value = 'Generation 1',
                        style = {'width': '200px'}, clearable= False
            ),
            html.Label("Choose strongest or weakest"),
            dcc.Dropdown(id = 'Strongest_Weakest_dropdown',
                        options = [
                            {'label': 'Strongest', 'value': 'Strongest'},
                            {'label': 'Weakest', 'value': 'Weakest'},
                        ],
                        value = 'Strongest',
                        style = {'width': '200px'}, clearable= False
            )
        ],
        style = {'margin-left': '60px'} # Moving the two dropdowns further to the right
        ),

    ]
    )
])



if __name__ == '__main__':
    app.run(debug=True)