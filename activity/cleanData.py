import random

def clean_data(data):
    """This cleans the data before sending the response.

    Returns:
        object: The response, including character name and sentence.
    """
    randint = random.randint(0, len(data['Character']))
    resp.message(data['Line'][randint])

    return str(resp)