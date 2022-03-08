from functions import get_df, write_df
import pandas as pd

"""
The function question2 first indexes out all rows containing data for ports with cargo wharf.
An aggregation of count is done within country group, followed by an ordering to obtain the
country with the largest number of ports.
"""

def question2(dataset_name):

    df = get_df()

    df_wharf = df[df['cargo_wharf'] == True]
    temp_df_wharf_agg = pd.DataFrame(df_wharf.groupby(['country'])['index_number'].count()).reset_index()
    df_wharf_agg = temp_df_wharf_agg.rename(columns={'index_number':'port_count'})
    answer2 = df_wharf_agg.sort_values(by='port_count',ascending=False).head(1)
    
    write_df(answer2, dataset_name, 'Table for Question 2')

if __name__ == "__main__":
    question2("foodpanda_tables")