import functions

def question2():
    df_wharf = df[df['cargo_wharf'] == True]
    temp_df_wharf_agg = pd.DataFrame(df_wharf.groupby(['country'])['index_number'].count()).reset_index()
    df_wharf_agg = temp_df_wharf_agg.rename(columns={'index_number':'port_count'})
    final = df_wharf_agg.sort_values(by='port_count',ascending=False)
    return final
