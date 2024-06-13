from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
import csv
import json
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static/files'

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        csv_data = csv.DictReader(file.read().decode('utf-8').splitlines())
        json_data = json.dumps([row for row in csv_data], indent=4)    
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename)))
        return jsonify(json.loads(json_data)) 

   

if __name__ == "__main__":
    app.run(debug=True)
