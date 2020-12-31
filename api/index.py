from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def welcome():
    return "Welcome to my awesome API ! "

@app.route('/api/', methods=['POST'])
def capture_email():
    email = request.form.get('email') # retrieve the email from the landing page
    name = request.form.get('name')
    cell = request.form.get('cell')
    return jsonify({"email": email, "name": name, "cell": cell })

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)