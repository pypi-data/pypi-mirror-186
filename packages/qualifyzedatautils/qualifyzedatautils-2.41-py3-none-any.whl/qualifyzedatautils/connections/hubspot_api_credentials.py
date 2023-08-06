import hubspot
from hubspot.crm.companies import ApiException
from ._decode_secret import decode_secret
from ._retrieve_awssecret import retrieve_awssecret

def initialize_hubspotapi_credentials():
    hubspotapi_secret = retrieve_awssecret("hubspot_api_qualifyzeaccess", "eu-central-1")
    hubspotapi_decoded_secret = decode_secret(hubspotapi_secret)
    hubspotapi_credentials = hubspotapi_decoded_secret

    return hubspotapi_credentials

def establish_hubspotapi_session():
    hubspotapi_credentials = initialize_hubspotapi_credentials()
    session = hubspot.Client.create(access_token=hubspotapi_credentials['application-key'])

    return session