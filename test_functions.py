import functions

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