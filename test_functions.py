import functions


def test_read_gen_db():
    df = functions.read_gen_db('Generation 1')
    assert df is not None
    assert len(df) > 0

    df_all_time = functions.read_gen_db('All Time')
    assert df_all_time is not None
    assert len(df_all_time) == len(functions.DF_STATS)


def test_filter_name_rows():
    row_index = 0
    filtered_df = functions.filter_name_rows(row_index)
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['name'] == functions.DF_STATS.loc[row_index, 'name']


def test_pokemon_image():
    pokemon_stats = [{'name': 'Pikachu'}]
    src = functions.pokemon_image(pokemon_stats)
    assert isinstance(src, str)
    assert src == '/assets/Pikachu.png'


def test_get_pokemon_stats():
    # Test Strongest - We have 1 row / 1 element in list
    data_strongest = functions.get_pokemon_stats('Generation 1', 'Strongest')
    assert isinstance(data_strongest, list)
    assert len(data_strongest) == 1

    # Test Weakest - We have 1 row / 1 element in list
    data_weakest = functions.get_pokemon_stats('Generation 1', 'Weakest')
    assert isinstance(data_weakest, list)
    assert len(data_weakest) == 1


def test_average_stats_graph():
    avg_row = functions.average_stats_graph('Generation 1')
    assert isinstance(avg_row, dict)
    assert avg_row['name'] == 'AVG Generation 1'
    assert len(avg_row['x']) == 7
    assert len(avg_row['y']) == 7


def test_pokemon_stats_graph():
    new_row_strongest = functions.pokemon_stats_graph('Generation 1', 'Strongest')
    assert isinstance(new_row_strongest, dict)
    assert len(new_row_strongest['x']) == 7
    assert len(new_row_strongest['y']) == 7

    new_row_weakest = functions.pokemon_stats_graph('Generation 1', 'Weakest')
    assert isinstance(new_row_weakest, dict)
    assert len(new_row_weakest['x']) == 7
    assert len(new_row_weakest['y']) == 7