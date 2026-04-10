"""
Flask App Routing file.
Email logic in corefunctions.py
"""

from flask import Flask, request, Response, jsonify
from flask_cors import CORS
import json
from corefunctions import csv_to_map, sendEmail, privacyAPI 

app = Flask(__name__)
cors = CORS(app, resources={r"/privacyAPI/*": {"origins": "http://localhost:3000"}})

# privacyAPI - initiates CCPA data delete requests
@app.route('/privacyAPI/v1/', methods=["POST"])
def executePrivacyAPI():
    '''
    This function runs the privacyAPI for live data brokers
    Cookie check: The cookie "live-test: true" is required to run this function
    '''
    usrjson = request.get_json()
    services = {}
    all_services, top_choice, people_search = csv_to_map("services_list_06May2021.csv")
    print("usrjson['usrchoice'] = ", usrjson['usrchoice'])
    if usrjson['usrchoice'] == 'all_services':
        services = all_services
    elif usrjson['usrchoice'] == 'top_choice':
        services = top_choice
    else:
        services = people_search
    return json.dumps({
        "return": privacyAPI(usrjson, services)
    }), 200

# Account creation endpoint
@app.route('/account/create', methods=['POST'])
def create_account():
    data = request.get_json()
    user_email = data.get('email')
    user_name = data.get('name')
    # Here you would typically add logic to create the user account in your database
    # For now, we'll just simulate this with a print statement
    print(f"Creating account for {user_name} with email {user_email}")
    
    # Send welcome email
    from email_service import EmailService
    from email_templates import ACCOUNT_CREATION_TEMPLATE
    
    email_service = EmailService('smtp.example.com', 465, 'your_email@example.com', 'your_password')
    email_body = ACCOUNT_CREATION_TEMPLATE.format(name=user_name)
    email_service.send_email(user_email, 'Welcome to Our Service', email_body)
    
    return jsonify({'message': 'Account created and email sent'}), 201

# Run Server
if __name__ == '__main__':
    app.run(debug=True)