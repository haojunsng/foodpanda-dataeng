from google.cloud import bigquery

def create_dataset(dataset_name):
    # Connecting to BigQuery Client using service account key (json) in config folder.
    bqclient = bigquery.Client.from_service_account_json('./config/foodpanda-assessment-343503-d4905b2cb42b.json')
    
    # Creates the dataset 'foodpanda_tables'
    dataset = bqclient.create_dataset(dataset_name, timeout=30)

if __name__ == "__main__":
    create_dataset("foodpanda_tables")