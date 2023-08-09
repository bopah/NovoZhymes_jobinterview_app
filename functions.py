import pandas as pd


read_stats = pd.read_csv('pokemon dataset/pokemon_stats.csv')
# I decided to remove name-duplicates and delete 'form'-column. This will provide faulty data,
# since some same-name pokemons have different forms which can affect their powerlevel.
# However the number of these cases are so small that I decided to ignore them for convenience sake.
# But its definitely something I would not do if I needed as close to 100% reliable data as possible!
drop_duplicates_stats = read_stats.drop_duplicates(subset=['name'])
delete_form = drop_duplicates_stats.drop('form', axis=1)
DF_STATS = delete_form.sort_values(by=read_stats.columns[0]) # Data Frame of all pokemon stats, which is sorted according to pokemon-index

# Read 1 of the 10 generation-database into a pandas dataFrame.
def read_gen_db(generation_dropdown):
    if generation_dropdown == 'All Time':
        df_sort = DF_STATS
        return df_sort
    else:
        gen_number = generation_dropdown[-1] # The last character is a number from 1-9
        data_path = 'pokemon dataset/pokemon_data_gen' + gen_number + '.csv'
        df = pd.read_csv(data_path)
        df_sort = df.sort_values(by=df.columns[0]) # Sort generation-data based on the first column (pokemon index)
        return df_sort