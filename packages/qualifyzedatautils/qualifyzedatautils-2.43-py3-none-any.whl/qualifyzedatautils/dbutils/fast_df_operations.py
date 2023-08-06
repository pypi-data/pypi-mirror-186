import sys, uuid, csv, random, string
import pandas as pd
import numpy as np
from ..s3utils.file_read import s3csvfile_todf
from ..s3utils.file_upload import df_tos3csvfile
from ..s3utils.file_delete import df_deletefile
from ..connections.dwh_awsservicer import initialize_dwhservicer_credentials, establish_dwhservicer_session


def fast_dataframe_dbupload(df, dbconnection, method, destination, unique_update_key, sep=",",
                            kwargs={'bucket-name': 'qualifyze-temporals', 'use-subfolder': True,
                                    'subfolder-full-path': 'df-batch-uploads'}):
    TMP_FILES_UUID = uuid.uuid1()
    BUCKET_NAME = kwargs['bucket-name']
    USE_SUBFOLDER = kwargs['use-subfolder']
    SUBFOLDER_PATH = kwargs['subfolder-full-path']
    TMP_FILE_PATH = {'bucket-name': BUCKET_NAME, 'use-subfolder': USE_SUBFOLDER, 'subfolder-full-path': SUBFOLDER_PATH,
                     'file-name': str(TMP_FILES_UUID)}

    def upload_tmp_file(df, tmp_file_path):
        S3FileUpload.df_tos3csvfile(df, destination=tmp_file_path)
        return 'Temporal File has been uploaded to S3'

    def retrieve_tmp_file(tmp_file_path):
        get_csv_structure = S3FileRead.s3csvfile_todf(filetoread=tmp_file_path)
        print('Temporary File has been retrieved from S3')
        return get_csv_structure

    def delete_tmp_file(tmp_file_path):
        tmp_file_path["file-name"] = str(tmp_file_path["file-name"]) + ".csv"
        S3FileDelete.df_deletefile(tmp_file_path)
        return print('Temporary File has been removed from S3')

    def get_colnames(df):
        column_names = []
        for col_name in df.columns:
            column_names.append(col_name)
        return column_names

    def copy_to_table(dbconnection, destination_table, tmp_uuid, sep):
        cursor = dbconnection.cursor()
        try:
            cursor.execute("COPY " + destination_table + " FROM 's3://qualifyze-temporals/df-batch-uploads/" + str(
                tmp_uuid) + ".csv' CREDENTIALS 'aws_access_key_id=AKIARKMPR272L4BKFYEC;aws_secret_access_key=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' DELIMITER '" + sep + "' IGNOREHEADER as 1;")
            print("Data inserted using copy_from_datafile() successfully....")
        except Exception as err:
            # os.remove(tmp_df)
            print(err)
        cursor.close()
        return 'Data was inserted into DWH'

    def create_tmp_table(dbconnection, tmp_uuid, column_names):
        tmp_staging_table_statement = 'CREATE TABLE dev.tmp_' + str(tmp_uuid).replace("-", "") + ' ('
        for i in column_names:
            tmp_staging_table_statement = (tmp_staging_table_statement + '\n' + '{} {}' + ',').format(i, 'varchar(max)')
        tmp_staging_table_statement = tmp_staging_table_statement[:-1] + ');'

        cursor = dbconnection.cursor()
        cursor.execute(tmp_staging_table_statement)
        cursor.close()

    def delete_tmp_table(dbconnection, tmp_uuid):
        cursor = dbconnection.cursor()
        cursor.execute("DROP TABLE IF EXISTS dev.tmp_" + str(tmp_uuid).replace("-", "") + ";")
        cursor.close()

    def get_operable_elements(df_existing, df_insert, unique_update_key, op_type):
        df_existingdata_id = df_existing['' + unique_update_key + ''].astype(str).values
        df_toupload_id = df_insert['' + unique_update_key + ''].astype(str).values
        if op_type == 'insert':
            unique_ids = np.setdiff1d(df_toupload_id, df_existingdata_id)
        elif op_type == 'update':
            unique_ids = np.intersect1d(df_toupload_id, df_existingdata_id)

        df_to_operate = df_insert[df_insert.eval(unique_update_key).isin(unique_ids)]
        return df_to_operate

    def main(df, dbconnection, method, destination, unique_update_key, tmp_uuid, tmp_file_path, sep=","):

        if method == 'insert':
            upload_tmp_file(df, tmp_file_path)
            copy_to_table(dbconnection, destination, tmp_uuid, sep)
            delete_tmp_file(tmp_file_path)

        elif method == 'upsert':
            upload_tmp_file(df, tmp_file_path)

            get_csv_structure = retrieve_tmp_file(tmp_file_path)
            column_names = get_colnames(get_csv_structure)
            create_tmp_table(dbconnection, tmp_uuid, column_names)
            copy_to_table(dbconnection, 'dev.tmp_' + str(tmp_uuid).replace("-", "") + '', tmp_uuid, sep)
            print('TMP Table has been created')

            cursor = dbconnection.cursor()
            cursor.execute("SELECT * FROM " + destination + "")
            result: tuple = cursor.fetchall()
            cursor.close()
            df_existingdata = pd.DataFrame(result, columns=column_names)
            print(df_existingdata)

            cursor = dbconnection.cursor()
            cursor.execute("SELECT * FROM dev.tmp_" + str(tmp_uuid).replace("-", "") + "")
            result: tuple = cursor.fetchall()
            cursor.close()
            df_toupload = pd.DataFrame(result, columns=column_names)
            print(df_toupload)

            df_records_to_insert = get_operable_elements(df_existingdata, df_toupload, unique_update_key, 'insert')
            tmp_file_path_insertfile = tmp_file_path.copy()
            tmp_file_path_insertfile["file-name"] = str(tmp_file_path_insertfile["file-name"]) + "_i"
            upload_tmp_file(df_records_to_insert, tmp_file_path_insertfile)
            copy_to_table(dbconnection, destination, str(tmp_uuid) + "_i", sep)
            print(df_records_to_insert)

            df_records_to_update = get_operable_elements(df_existingdata, df_toupload, unique_update_key, 'update')
            tmp_file_path_updatefile = tmp_file_path.copy()
            tmp_file_path_updatefile["file-name"] = str(tmp_file_path_updatefile["file-name"]) + "_u"
            upload_tmp_file(df_records_to_update, tmp_file_path_updatefile)
            print(df_records_to_update)

            elements_to_update = df_records_to_update['' + unique_update_key + ''].tolist()
            elements_to_update_statementquery = f"({', '.join(elements_to_update)})"
            print(elements_to_update_statementquery)

            cursor = dbconnection.cursor()
            cursor.execute("DELETE FROM " + str(destination) + " WHERE " + str(unique_update_key) + " in " + str(
                elements_to_update_statementquery) + "")
            cursor.close()

            copy_to_table(dbconnection, destination, str(tmp_uuid) + "_u", sep)

            # Cleaning S3 Temp Files
            #delete_tmp_table(dbconnection, tmp_uuid)
            #delete_tmp_file(tmp_file_path_insertfile)
            #delete_tmp_file(tmp_file_path_updatefile)


        else:
            print(f'The selected method [ {method} ] does not exist - Available methods: insert, upsert')

    if __name__ == "__main__":
        main(df, dbconnection, method, destination, unique_update_key, TMP_FILES_UUID, TMP_FILE_PATH, sep=",")

