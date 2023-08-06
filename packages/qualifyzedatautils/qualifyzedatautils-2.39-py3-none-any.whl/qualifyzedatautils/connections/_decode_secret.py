import json
import base64

def decode_secret(secret):
    '''

    Function to decode the Secret by:
        1) Loading it into a JSON
        2) Decoding the base64 String
        3) Cleansing system characters
        4) returning again into a JSON

    As input takes the Secret as retrieved from AWS Secret Manager

    :param secret:
    :return: JSON with credential details
    '''
    load_secret_to_json = json.loads(secret)
    decoded_credentials = base64.b64decode(load_secret_to_json['credentials'])
    set_ascci = decoded_credentials.decode("ascii")
    final_json = json.loads(set_ascci)

    return final_json