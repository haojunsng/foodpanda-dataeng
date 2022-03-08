from google.cloud import bigquery

def get_df():
    
    # Connecting to BigQuery Client using service account key (json) in config folder.
    bqclient = bigquery.Client.from_service_account_json('./config/foodpanda-assessment-343503-d4905b2cb42b.json')
    
    # Reading in and converting it to a dataframe for data analysis
    df = bqclient.list_rows('bigquery-public-data.geo_international_ports.world_port_index').to_dataframe()
    return df

def write_df(dataframe, table_name):
    
    # Connecting to BigQuery Client using service account key (json) in config folder.
    bqclient = bigquery.Client.from_service_account_json('./config/foodpanda-assessment-343503-d4905b2cb42b.json')
    
    dataset = bqclient.get_dataset('foodpanda-assessment-343503.foodpanda_tables')

    # Configuring the write_disposition for LoadJobConfig: WRITE_TRUNCATE --> overwrites the table if exists
    job_config = bigquery.LoadJobConfig(
        write_disposition=bigquery.job.WriteDisposition.WRITE_TRUNCATE
    )

    # insert table
    job = bqclient.load_table_from_dataframe(
        dataframe=dataframe,
        destination=dataset.table(table_name),
        job_config=job_config
    )
    
    job.result()