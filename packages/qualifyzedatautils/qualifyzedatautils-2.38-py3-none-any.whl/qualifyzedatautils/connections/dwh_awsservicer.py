import boto3
from ._decode_secret import decode_secret
from ._retrieve_awssecret import retrieve_awssecret

def initialize_dwhservicer_credentials():
    dwhservicer_secret = retrieve_awssecret("dwh_awsservicer", "eu-central-1")
    dwhservicer_decoded_secret = decode_secret(dwhservicer_secret)
    dwhservicer_credentials = dwhservicer_decoded_secret

    return dwhservicer_credentials

def establish_dwhservicer_session():
    dwhservicer_credentials = initialize_dwhservicer_credentials()
    session = boto3.Session(
        aws_access_key_id=dwhservicer_credentials['aws_access_key_id'],
        aws_secret_access_key=dwhservicer_credentials['aws_secret_access_key']
    )

    return session