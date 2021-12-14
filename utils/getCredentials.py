import os

def get_credentials():
    """This gets the twilio credentials.

    Returns:
        object: a Client object connected to the twilio api.
    """
    account_sid = os.environ.get('twilio_sid')
    auth_token = os.environ.get('twilio_token')

    return account_sid, auth_token