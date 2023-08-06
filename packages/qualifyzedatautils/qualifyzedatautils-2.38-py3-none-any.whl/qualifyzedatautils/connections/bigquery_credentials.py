
from google.cloud import bigquery
from google.oauth2 import service_account
from ._decode_secret import decode_secret
from ._retrieve_awssecret import retrieve_awssecret

def initialize_bigquery_credentials():
    bigquery_secret = retrieve_awssecret("bigquery_credentials", "eu-central-1")
    bigquery_decoded_secret = decode_secret(bigquery_secret)
    bigquery_credentials = bigquery_decoded_secret

    return bigquery_credentials

def establish_bigquery_connection(projectid):
    bigquery_credentials = initialize_bigquery_credentials()
    project_id = projectid
    credentials = service_account.Credentials.from_service_account_info(bigquery_credentials)
    client = bigquery.Client(credentials=credentials, project=project_id)

    return client