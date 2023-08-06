
from ..connections.dwh_awsservicer import initialize_dwhservicer_credentials, establish_dwhservicer_session
from io import StringIO


def df_tos3csvfile(dfobject, destination):

    session = establish_dwhservicer_session()

    s3_res = session.resource('s3')
    csv_buffer = StringIO()
    dfobject.to_csv(csv_buffer, index=False)

    bucket_name = destination['bucket-name']
    s3_object_name = destination['file-name']+'.csv'

    if destination['use-subfolder']==True:
        s3_res.Object(bucket_name, s3_object_name).put(Key=destination['subfolder-full-path']+"/"+destination['file-name']+".csv", Body=csv_buffer.getvalue())
    else:
        s3_res.Object(bucket_name, s3_object_name).put(Body=csv_buffer.getvalue())

    return print("File has been uploaded!")
