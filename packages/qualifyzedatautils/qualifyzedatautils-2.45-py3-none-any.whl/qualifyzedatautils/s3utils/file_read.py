
from ..connections.dwh_awsservicer import initialize_dwhservicer_credentials, establish_dwhservicer_session
from io import StringIO
import pandas as pd

def s3csvfile_todf(filetoread):

    session = establish_dwhservicer_session()

    client = session.client('s3')

    bucket_name = filetoread['bucket-name']
    s3_object_name = filetoread['file-name'] + '.csv'

    if filetoread['use-subfolder']==True:
        csv_obj = client.get_object(Bucket=bucket_name, Key=filetoread['subfolder-full-path']+"/"+filetoread['file-name']+".csv")
    else:
        csv_obj = client.get_object(Bucket=bucket_name, Key=s3_object_name)

    body = csv_obj['Body']
    csv_string = body.read().decode('utf-8')
    df = pd.read_csv(StringIO(csv_string))

    return df



