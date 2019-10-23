import base64
import json
from google.api_core import retry
from google.cloud import bigquery

BQ_DATASET = 'semana_i'
BQ_TABLE = 'telemetry'
BQ = bigquery.Client()

schema = [
        bigquery.SchemaField('ts', 'TIMESTAMP', mode='NULLABLE'),
        bigquery.SchemaField('temperature', 'INTEGER', mode='NULLABLE'),
        bigquery.SchemaField('pressure', 'FLOAT', mode='NULLABLE'),
        bigquery.SchemaField('humidity', 'FLOAT', mode='NULLABLE')
        ]

def process_data(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
        event (dict): Event payload.
        context (google.cloud.functions.Context): Metadata for the event.
    """
    pubsub_message = json.loads(base64.b64decode(event['data']).decode('utf-8'))

    print(pubsub_message)
    try:
        _insert_into_bigquery(pubsub_message)
            
    except  BigQueryError as e:
        print(e.errors)
    

def _insert_into_bigquery(message):
    table = BQ.dataset(BQ_DATASET).table(BQ_TABLE)
    
    errors = BQ.insert_rows(table, [message], selected_fields = schema )
    if errors != []:
        raise BigQueryError(errors)

    
class BigQueryError(Exception):
    '''Exception raised whenever a BigQuery error happened''' 

    def __init__(self, errors):
        super().__init__(self._format(errors))
        self.errors = errors

    def _format(self, errors):
        err = []
        for error in errors:
            err.extend(error['errors'])
        return json.dumps(err)
