from datetime import datetime
import redshift_connector

def post_sanitylog( redshift_valid_connection, type, source, affected, response="" ):

    insertion_ts = datetime.now()

    try:
        cursor_sanitylog = redshift_valid_connection.cursor()
        cursor_sanitylog.execute('INSERT INTO dev.sanity_logs (type, source, affected, response, log_ts) VALUES (%s, %s, %s, %s, %s)', (type, source, affected, response, insertion_ts))
        cursor_sanitylog.close()
        redshift_valid_connection.commit()

        print("The Sanity Log was successfully inserted!")
    except:
        print(
            "The Sanity Log was not inserted. A problem occurred during the execution of the process. Please review that all your inputs are valid.")