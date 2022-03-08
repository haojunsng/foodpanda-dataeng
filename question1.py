import functions

def question1():

    df = get_df()

    sg_jurong_island = df[(df['country']=='SG') & (df['port_name']=='JURONG ISLAND')]
    sg_jurong_island_coords = (float(sg_jurong_island['port_latitude']), float(sg_jurong_island['port_longitude']))

    df_without_jurong_island = pd.concat([df,sg_jurong_island]).drop_duplicates(keep=False)
    results = []

    for each in df_without_jurong_island.itertuples(index=False):
        port_name = each[2]
        each_coords = (float(each[4]), float(each[5]))
        dist = geopy.distance.geodesic(sg_jurong_island_coords, each_coords)
        results.append(dist)
        
    df_without_jurong_island['dist'] = results
    nearest_5_ports = df_without_jurong_island.sort_values(by='dist', ascending=True).head()
    answer1 = nearest_5_ports[['port_name', 'dist']].reset_index(drop=True)

    write_df(answer1, 'Table for Question 1')

if __name__ == "__main__":
    question1()