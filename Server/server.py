from flask import Flask, request
from controller.controller import controller
import os
from flask import Flask, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from flask_cors import CORS

# UPLOAD_FOLDER = Path.cwd() / '/uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
CORS(app)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
controllerObj = controller()

localPaths = ['3D Objects', 'Desktop', 'Documents', 'Downloads', 'Music', 'Pictures', 'Videos', 'C:\\']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    # print(f'query: {request.query_string}')
    return 'Hello World'

@app.route('/uploadFile', methods=['POST'])
def getMP3File():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return 'File not found', 404
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return 'File not selected', 404
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)    
            dst = request.form['conversionDST']
            conversionType = request.form['conversionType']
            
            src = controllerObj.saveFile(file, filename)

            if conversionType == 'mp3':
                return controllerObj.convertFileToMP3(src = src, dst=dst, filename=filename)
            
            elif conversionType == 'wav-16bit':
                return controllerObj.convertFileToWAV(src=src, filename=filename, wav='16bit', dst=dst)
            
            elif conversionType == 'wav-32bit':
                return controllerObj.convertFileToWAV(src=src, filename=filename, wav='32bit', dst=dst)
            
            else:
                return f'error conversion type not found for {conversionType}', 404
            
if __name__ == "__main__":
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port)
