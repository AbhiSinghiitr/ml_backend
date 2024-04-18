from flask import Flask, request, jsonify
from voice_classifier import get_class

app = Flask(__name__)

# Function to process voice input and return map object
def process_voice_input(voice_data):
    
    cl= get_class(voice_data)

    
    map_object = {
        "out": cl
    }
    
    return map_object

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/process_voice', methods=['POST'])
def process_voice():
    if 'voice_data' not in request.files:
        return jsonify({'error': 'No voice data found'}), 400

    # voice_file = request.files['voice_data']
    map_object = process_voice_input('aud.wav')

    return jsonify(map_obj)
