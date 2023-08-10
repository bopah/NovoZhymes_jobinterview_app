import functions

def test_read_gen_db():
    df = functions.read_gen_db('Generation 1')
    assert df is not None
    assert len(df) > 0

    df_all_time = functions.read_gen_db('All Time')
    assert df_all_time is not None
    assert len(df_all_time) == len(functions.DF_STATS)


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