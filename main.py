from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
import requests

from utils.getCredentials import get_credentials
from activity.getData import get_data
from activity.cleanData import clean_data

app = Flask(__name__)
Bootstrap(app)

### Web pages ###
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/sms/", methods=['GET', 'POST'])
def sms_reply():

    data = get_data()
    response = clean_data(data)
    return response

if __name__ == '__main__':
    app.run(debug=False)
