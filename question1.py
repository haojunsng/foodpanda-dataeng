import functions

"""
The function question1() first isolates the row for Singapore's Jurong Island Port.
A for loop is run to compute the geodesic distance (a shortest arc between 2 points on a curved surface - Earth)
between Singapore's Jurong Island Port and every other port in the dataframe.
The computed geodesic distance is then appended as a column and the dataframe is sorted by that column.
The top 5 nearest ports are obtained after sorting.
"""

def question1(dataset_name):

    df = get_df()

    sg_jurong_island = df[(df['country']=='SG') & (df['port_name']=='JURONG ISLAND')]
    sg_jurong_island_coords = (float(sg_jurong_island['port_latitude']), float(sg_jurong_island['port_longitude']))

    df_without_jurong_island = pd.concat([df,sg_jurong_island]).drop_duplicates(keep=False)
    results = []

    for each in df_without_jurong_island.itertuples(index=False):
        each_coords = (float(each[4]), float(each[5]))
        dist = geopy.distance.geodesic(sg_jurong_island_coords, each_coords)
        results.append(dist)
        
    df_without_jurong_island['dist'] = results
    nearest_5_ports = df_without_jurong_island.sort_values(by='dist', ascending=True).head()
    answer1 = nearest_5_ports[['port_name', 'dist']].reset_index(drop=True)

    write_df(answer1, dataset_name, 'Table for Question 1')

if __name__ == "__main__":
    question1("foodpanda_tables")