from ..connections.dwh_awsservicer import initialize_dwhservicer_credentials, establish_dwhservicer_session

def file_copyrename(originfile, destinationfile, is_rename_operation):

    session = establish_dwhservicer_session()
    client = session.resource('s3')

    if originfile['use-subfolder']==True:
        copy_source = {
            'Bucket': ''+originfile["bucket-name"]+'',
            'Key': ''+originfile['subfolder-full-path']+"/"+originfile['file-name-withext']+''
        }
    else:
        copy_source = {
            'Bucket': ''+originfile["bucket-name"]+'',
            'Key': ''+originfile['file-name-withext']+''
        }

    bucket = client.Bucket(''+destinationfile["bucket-name"]+'')

    if destinationfile['use-subfolder'] == True:
        bucket.copy(copy_source, ''+destinationfile['subfolder-full-path']+"/"+destinationfile['file-name-withext']+'')
    else:
        bucket.copy(copy_source, ''+destinationfile['file-name-withext']+'')

    if is_rename_operation==True:
        if originfile['use-subfolder']==True:
            client.Object(''+originfile["bucket-name"]+'', ''+originfile['subfolder-full-path']+"/"+originfile['file-name-withext']+'').delete()
        else:
            client.Object('' + originfile["bucket-name"] + '', ''+originfile['file-name-withext']+'').delete()











