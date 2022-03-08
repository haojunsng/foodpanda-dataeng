from functions import get_df, write_df
import geopy
from geopy import distance

"""
The function question3 takes in the latitude and longitude of potential distress locations,
and returns the nearest port with essential provisions such as water, fuel_oil and diesel.
"""

def question3(dataset_name, latitude, longitude):

    df = get_df()

    distress_location = (latitude, longitude)
    ports_with_provisions = df[(df['provisions'] == True) & (df['water'] == True) & (df['fuel_oil'] == True) & (df['diesel'] == True)]
    results = []

    for each in ports_with_provisions.itertuples(index=False):
        each_coords = (float(each[4]), float(each[5]))
        dist = geopy.distance.geodesic(distress_location, each_coords)
        results.append(dist.km)

    ports_with_provisions['dist'] = results
    answer3 = ports_with_provisions.sort_values(by='dist', ascending=True)[['country', 'port_name', 'port_latitude', 'port_longitude']].head(1)

    write_df(answer3, dataset_name, 'Table for Question 3')

if __name__ == "__main__":
    question3("foodpanda_tables", 32.610982, -38.706256)
