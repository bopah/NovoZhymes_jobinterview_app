import pandas as pd

# I decided to remove name-duplicates and delete 'form'-column. This will provide faulty data,
# since some same-name pokemons have different forms which can affect their powerlevel.
# However the number of these cases are so small that I decided to ignore them for convenience sake.
# But its definitely something I would not do if I needed as close to 100% reliable data as possible!
read_stats = pd.read_csv('pokemon dataset/pokemon_stats.csv')
drop_duplicates_stats = read_stats.drop_duplicates(subset=['name'])
delete_form = drop_duplicates_stats.drop('form', axis=1)
DF_STATS = delete_form.sort_values(by=read_stats.columns[0])  # Data Frame of all pokemon stats, which is sorted according to pokemon-index

# Read 1 of the 10 generation-database into a pandas dataFrame.
def read_gen_db(generation_dropdown):
    if generation_dropdown == 'All Time':
        df_sort = DF_STATS
        return df_sort
    else:
        gen_number = generation_dropdown[-1]  # The last character is a number from 1-9
        data_path = 'pokemon dataset/pokemon_data_gen' + gen_number + '.csv'
        df = pd.read_csv(data_path)
        df_sort = df.sort_values(by=df.columns[0])  # Sort generation-data based on the first column (pokemon index)
        return df_sort

# Filters all the rows for a specific name.
def filter_name_rows(row_index):
    name = DF_STATS.loc[row_index, 'name']  # the value of the 'name' column
    filter = DF_STATS[DF_STATS['name'] == name]  # filtering the entire data set, so we only have a dataset with 1 row
    return filter

# Return path an image of the pokemon
def pokemon_image(pokemon_stats):
    name = pokemon_stats[0]['name']  # pokemon_stats is a list of dictionaries with only 1 element, which is why we '[0]'
    src = '/assets/' + name + '.png'
    return src

# We have 9 different Generation-datasets, and 1 stats-dataset which includes all the pokemons from all the generations.
# Finds the amount of pokemons in the selected generation by finding the first and last pokemon-index and then apply slicing.
# Then we use the stats-dataset to find the max/min of the 'total'-column, from first to last pokemon-index.
# Returns a list of dictionaries of one specific row from the stats-dataset (so a list with only 1 element).
def get_pokemon_stats(generation_dropdown, strongest_weakest_dropdown):
    df_generation = read_gen_db(generation_dropdown)
    first_index_value = df_generation.iloc[0, 0] - 1  # -1 since we 0-index
    last_index_value = df_generation.iloc[-1, 0]

    if strongest_weakest_dropdown == 'Strongest':
        strongest_index = DF_STATS.iloc[first_index_value:last_index_value]['total'].idxmax()  # idx of the row with MAX-value in 'total' column
        filter = filter_name_rows(strongest_index)
        data = filter.to_dict('records')  # Converting the row to a dictionary so it can be used in 'dash_table.DataTable-data' property
        return data
    elif strongest_weakest_dropdown == 'Weakest':
        weakest_index = DF_STATS.iloc[first_index_value:last_index_value]['total'].idxmin()  # idx of the row with MIN-value in 'total' column
        filter = filter_name_rows(weakest_index)
        data = filter.to_dict('records')  # Converting the row to a dictionary so it can be used in 'dash_table.DataTable-data' property
        return data

# Returns a dictionary of a new row-dataset with only actual stats (i.e no 'name) to be used in a graph.
# The new dataset consists of the average stats of all pokemons from the selected Generation-dataset-dropdown.
def average_stats_graph(generation_dropdown):
    df_generation = read_gen_db(generation_dropdown)
    first_index_value = df_generation.iloc[0, 0] - 1  # -1 since we 0-index
    last_index_value = df_generation.iloc[-1, 0]

    # Finding the mean/average of every stat column
    avg_total = DF_STATS.iloc[first_index_value:last_index_value]['total'].mean()
    avg_hp = DF_STATS.iloc[first_index_value:last_index_value]['hp'].mean()
    avg_attack = DF_STATS.iloc[first_index_value:last_index_value]['attack'].mean()
    avg_defense = DF_STATS.iloc[first_index_value:last_index_value]['defense'].mean()
    avg_sp_atk = DF_STATS.iloc[first_index_value:last_index_value]['sp_atk'].mean()
    avg_sp_def = DF_STATS.iloc[first_index_value:last_index_value]['sp_def'].mean()
    avg_speed = DF_STATS.iloc[first_index_value:last_index_value]['speed'].mean()

    # The new row dictionary
    avg_row = {'x': ['total', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed'],
               'y': [avg_total, avg_hp, avg_attack, avg_defense, avg_sp_atk, avg_sp_def, avg_speed], 'type': 'bar', 'name': 'AVG ' + generation_dropdown}
    return avg_row

# Helper function for pokemon_stats_graph
def helper_pokemon_stats_graph(data_row):
    total = data_row.iloc[0, data_row.columns.get_loc('total')]
    hp = data_row.iloc[0, data_row.columns.get_loc('hp')]
    attack = data_row.iloc[0, data_row.columns.get_loc('attack')]
    defense = data_row.iloc[0, data_row.columns.get_loc('defense')]
    sp_atk = data_row.iloc[0, data_row.columns.get_loc('sp_atk')]
    sp_def = data_row.iloc[0, data_row.columns.get_loc('sp_def')]
    speed = data_row.iloc[0, data_row.columns.get_loc('speed')]
    name = data_row.iloc[0, data_row.columns.get_loc('name')]

    new_row = {'x': ['total', 'hp', 'attack', 'defense', 'sp_atk', 'sp_def', 'speed'],
               'y': [total, hp, attack, defense, sp_atk, sp_def, speed], 'type': 'bar', 'name': name}
    return new_row

# Returns a dictionary of a new row-dataset with only actual stats (i.e no 'name) to be used in a graph.
# The new dataset consists of the stats of the selected strongest/weakest pokemon
def pokemon_stats_graph(generation_dropdown, strongest_weakest_dropdown):
    # Read a dataset into a pandas Data Frame
    df_generation = read_gen_db(generation_dropdown)
    first_index_value = df_generation.iloc[0, 0] - 1  # -1 since we 0-index
    last_index_value = df_generation.iloc[-1, 0]

    if strongest_weakest_dropdown == 'Strongest':
        strongest_index = DF_STATS.iloc[first_index_value:last_index_value]['total'].idxmax()  # idx of the row with max-value in 'total' column
        filter = filter_name_rows(strongest_index)
        new_row = helper_pokemon_stats_graph(filter)
        return new_row
    elif strongest_weakest_dropdown == 'Weakest':
        weakest_index = DF_STATS.iloc[first_index_value:last_index_value]['total'].idxmin()  # idx of the row with min-value in 'total' column
        filter = filter_name_rows(weakest_index)
        new_row = helper_pokemon_stats_graph(filter)
        return new_row
