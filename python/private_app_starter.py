import os
from dotenv import load_dotenv
from hubspot import HubSpot
from flask import Flask, request

# please, set FLASK_APP in your .env file
app = Flask(__name__)

# use home path
@app.route("/hubspot/webhook", methods=['GET', 'POST'])
def webhook():
  api_client = HubSpot()    # get hubspot client
  api_client.access_token = access_token()    # set your private app access token
  request_data = request.get_json()
  print(request_data[0]["objectId"])
  quote_data=api_client.crm.objects.basic_api.get_by_id("quotes", request_data[0]["objectId"])
  if quote_data["prperties"]["hs_status"]=="DRAFT":
    print("new Draft")
    return("200")
  print(quote_data)
  return request_data   # return your contacts as json
  

# get access_token from .env file
def access_token():
  load_dotenv()
  return os.environ['ACCESS_TOKEN']
