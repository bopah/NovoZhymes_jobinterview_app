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

    # Add more test cases as needed