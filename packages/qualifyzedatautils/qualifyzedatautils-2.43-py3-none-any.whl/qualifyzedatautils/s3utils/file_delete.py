from ..connections.dwh_awsservicer import initialize_dwhservicer_credentials, establish_dwhservicer_session

def df_deletefile(filetodelete):

    session = establish_dwhservicer_session()
    s3 = session.resource('s3')

    if filetodelete['use-subfolder']==True:
        s3.Object(filetodelete['bucket-name'], filetodelete['subfolder-full-path']+"/"+filetodelete['file-name']).delete()
    else:
        s3.Object(filetodelete['bucket-name'], filetodelete['file-name']).delete()
