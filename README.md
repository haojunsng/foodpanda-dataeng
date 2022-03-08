# Sng Hao Jun
Foodpanda Data Engineering Technical Assessment

## Setting Up
- Python 3.10.2
- pandas 1.4.1  ```pip install pandas```
- geopy 2.2.0  ```pip install geopy```
- google-cloud-bigquery 2.34.2  ```pip install google-cloud-bigquery```

1. Create a Google Cloud Account
2. Create Google Service Account and download the service account key (.json) file
3. Save the service account key (.json) file in a folder named 'config'

## Codes to Run

1. Run ```python setup.py``` first to create the dataset in BigQuery.
2. Run ```python question1.py``` to read the data from BigQuery as well as to load the output table in the dataset created in step 1.
3. Do the same for ```python question2.py``` and ```python question3.py``` .
4. Output results can be viewed in this [link](https://console.cloud.google.com/bigquery?project=foodpanda-assessment-343503).

### Question 1
- To obtain the 5 nearest ports to Singapore's Jurong Island port, first retrieve the row of data that represents said port.
- Run an iterative for loop to calculate the geodesic distance (a shortest arc between 2 points on a curved surface - Earth) between Singapore's Jurong Island port and every other port.
- To calculate the geodesic distance, the geopy package is very helpful using geopy.distance.
- Finally, simply sort the data in ascending order and retrieve the top 5 rows.

### Question 2
- Subset out the portion of data where ports come with a cargo wharf.
- Perform an aggregation using count function within the country group.
- Order the output in descending order and retrieve the top row as the country with the largest number of ports.

### Question 3
- Subset out the portion of data where essential provisions are available - i.e. provisions, water, fuel_oil and diesel == True.
- Similar to Question 1, run an iterative for loop to calculate the geodesic distances between the location of distress call and every other port in the portion of data retrieved earlier.
- Conduct a sort in ascending order to retrieve the nearest port with said provisions.
