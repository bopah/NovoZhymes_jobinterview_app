from dash import Dash, dcc, html, dash_table, Input, Output
import functions

app = Dash(__name__)

app.layout = html.Div([
    # Title
    html.H1(
        children="Explore the stats of the strongest or weakest Pokémon from each generation",
        style={'fontSize': '40px', 'textAlign': 'center'}
    ),

    # Wrapping the two dropdowns and stats+image+graph together, so I can place them side by side
    html.Div(children=[
        # Wrapping the two dropdowns together
        html.Div(children=[
            html.Label("Choose a Generation"),
            dcc.Dropdown(
                id='Gen_dropdown',
                options=[
                    {'label': f'Generation {i}', 'value': f'Generation {i}'}
                    for i in range(1, 10)
                ] + [{'label': 'All Time', 'value': 'All Time'}],
                value='Generation 1',
                style={'width': '200px'}, clearable=False
            ),
            html.Label("Choose strongest or weakest"),
            dcc.Dropdown(
                id='Strongest_Weakest_dropdown',
                options=[
                    {'label': 'Strongest', 'value': 'Strongest'},
                    {'label': 'Weakest', 'value': 'Weakest'},
                ],
                value='Strongest',
                style={'width': '200px'}, clearable=False
            )
        ],
            style={'margin-left': '60px'}  # Moving the two dropdowns further to the right
        ),

        # Wrapping stats+image+graph
        html.Div(children=[
            html.Label("Stats"),
            dash_table.DataTable(
                id='Stats',
                page_size=1,
                style_cell={"width": "5%"}
            ),
            html.Img(id='Pokemon_image'),  # Add the image here
            dcc.Graph(id='Graph')  # Add the graph here
        ],
            style={'margin-left': '40px'}  # Moving stats+image+graph components further to the right
        )
    ],
        style={'display': 'flex', 'flex-direction': 'row'}  # Placing the two wrapped components (dropdowns and stats+image+graph) side by side
    )
])

# Callback for updating stats and graph
@app.callback(
    Output(component_id='Stats', component_property='data'),
    Output(component_id='Pokemon_image', component_property='src'),
    Output(component_id='Graph', component_property='figure'),
    Input(component_id='Gen_dropdown', component_property='value'),
    Input(component_id='Strongest_Weakest_dropdown', component_property='value')
)
def update(generation_dropdown, strongest_Weakest_dropdown):
    # First output, which changes the stats table
    pokemon_stats = functions.get_pokemon_stats(generation_dropdown, strongest_Weakest_dropdown)

    # Second output, which changes stats graph
    pokemon_image = functions.pokemon_image(pokemon_stats)

    # Third output, which changes image
    avg_stats = functions.average_stats_graph(generation_dropdown)
    pokemon_stats_graph = functions.pokemon_stats_graph(generation_dropdown, strongest_Weakest_dropdown)
    stats_graph = [avg_stats, pokemon_stats_graph]
    figure_data = {
        'data': stats_graph,
        'layout': {
            'xaxis': {'showgrid': True, 'gridcolor': 'lightgray'},
            'yaxis': {'showgrid': True, 'gridcolor': 'lightgray', 'dtick': 100},
            'title': 'Comparison of Pokémon Stats: Average of selected Generation vs. Resulting Pokémon'
        }
    }
    return pokemon_stats, pokemon_image, figure_data


if __name__ == '__main__':
    app.run_server(host="0.0.0.0", port=8050, debug=True)
