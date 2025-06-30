from flask import Flask, request
from controller.controller import controller
import os
from flask import Flask, flash, redirect, url_for
from werkzeug.utils import secure_filename
from pathlib import Path
from flask_cors import CORS


def init():
    if not Path(Path.cwd() / 'uploads').exists():
        Path.mkdir(Path.cwd() / 'uploads')
    if not Path(Path.cwd() / 'converted').exists():
        Path.mkdir(Path.cwd() / 'converted')



# UPLOAD_FOLDER = Path.cwd() / '/uploads'
ALLOWED_EXTENSIONS = {'mp4'}

app = Flask(__name__)
CORS(app)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
controllerObj = controller()




def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def hello():
    print(f'query: {request.query_string}')
    return 'Hello World'

@app.route('/uploadFileToMP3', methods=['POST'])
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
            src = controllerObj.saveFile(file, filename)
            queryParams = request.query_string.decode('utf-8')
            for i, v in request.form.items():
                print(i, v)

            if 'filedst' not in queryParams:
                dst = None
            else:
                dst = queryParams.split('=')[1]
            
            # controllerObj.convertFileToMP3(src = src, dst=dst, filename=filename)
            return 'ok', 200

@app.route('/uploadFileToWAV', methods=['POST'])
def getWAVFile():
    if request.method == 'POST':
        print('dasdsa')
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
            src = controllerObj.saveFile(file, filename)
            query = request.query_string.decode('utf-8')
            if '&' in query:
                wav, dst = request.query_string.decode('utf-8').split('&')
                wav = wav.split('=')[1]
                dst = dst.split('=')[1]
            else:
                wav = query.split('=')[1] # params format NEEDS to be wav: 16bit or wav: 32bit
                dst=None
            
            if wav != '16bit' and wav != '32bit':
                return f'INCORRECT WAV PARAMS FORMAT: {request.query_string}, PARSED WAV=: {wav}', 400
            
            controllerObj.convertFileToWAV(src=src, filename=filename, wav=wav, dst=dst)
            return 'ok', 200
        else:
            print('no file or file not allowed for ', file.filename)

if __name__ == "__main__":
    init()
    host = '127.0.0.1'
    port = 8080
    app.run(host=host, port=port)
