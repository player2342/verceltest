from flask import Flask
from flask import jsonify
from flask import request

from airtable import Airtable # import Airtable API python wrapper

#Set airtable base infortion and API key
base_key = 'appnGSTKWu1qD4Xaj' 
table_name = 'Table 1'
air_table_api_key = 'keymABXgPYp3BUmSL'
airtable = Airtable(base_key, table_name, api_key=air_table_api_key)


app = Flask(__name__)
@app.route('/', defaults={'path': ''})
@app.route('/', methods=['GET'])    # define landing page route and serve the static file
def welcome():
    return "Welcome to my awesome API"

@app.route('/api/', methods=['POST']) # define the email capturing api route to /api/
def capture_email():
    form_values = request.form.to_dict()    #retrieve form values
    airtable.insert(form_values)            #insert values in airtable
    return jsonify(request.form.to_dict())  

@app.after_request                      # allow request to come from any origin
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)