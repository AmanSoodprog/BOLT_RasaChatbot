import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Define the Rasa server URL
RASA_SERVER_URL = 'http://localhost:5005/webhooks/rest/webhook'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    
    message = request.form['message']


    response = requests.post(RASA_SERVER_URL, json={'message': message})
    response_data = response.json()
    chatbot_response = response_data[0]['text']
 
    return render_template('index.html', message=message, chatbot_response=chatbot_response)
# @app.route('/chatbot', methods=['POST'])
# def chatbot():
#     # Get the messages from the form
#     messages = request.form.getlist('message')

#     # Send the messages to the Rasa server
#     response = requests.post(RASA_SERVER_URL, json={'messages': messages})

#     # Extract the chatbot's responses from the Rasa server's response
#     response_data = response.json()
#     chatbot_responses = [r['text'] for r in response_data]

#     # Render the chatbot's responses in the HTML template
#     return render_template('index.html', messages=messages, chatbot_responses=chatbot_responses)

if __name__ == '__main__':
    app.run(debug=True,port=5010)
