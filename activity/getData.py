import pandas as pd

def get_data():
    """This gets the character name and sentence from the user's text message.

    Returns:
        object: The character name and sentence.
    """
    data = pd.read_csv("../utils/TheOfficeSMS.csv")
    data['Character'] = data['Character'].str.lower()
    resp = MessagingResponse()
    body = request.values.get("Body", None).lower().strip().replace(" ","")
    data = data[data['Character'] == str(body)].reset_index(drop=True)

    return data