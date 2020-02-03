
# A very simple Flask Hello World app for you to get started with...

from flask import Flask , request , render_template , flash , redirect , url_for
from werkzeug.utils import secure_filename
import os
import urllib.request
from app import app
import mido
from mido import MidiFile, MidiTrack, Message, MetaMessage
from os import listdir
from os.path import isfile, split, join
import argparse
import staffnotes
import split
import splittowav
import wavtospec



#UPLOAD_FOLDER = '/test'
ALLOWED_EXTENSIONS = set(['mid', 'mp3'])

#app = Flask(__name__)
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


app.config["DEBUG"] = True

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
	return render_template('index.html')

@app.route("/", methods=["GET","POST"])
def index():
	if request.method == 'POST':
        # check if the post request has the file part
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file = request.files['file']
		if file.filename == '':
			flash('No file selected for uploading')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			flash('File successfully uploaded')
			
			split.main()
			
			splittowav.splittowav()

			wavtospec.wavtospec()

			staffnotes.all()
			
			return redirect('/')
		else:
			flash('Allowed file types are mp3,mid')
			return redirect(request.url)



#split.main()

#splittowav.splittowav()

#wavtospec.wavtospec()

#staffnotes.all()

#def index():
#    return render_template('index.html')
@app.route("/logn", methods=["GET","POST"])
def logn():
	return render_template('logn.html')
if __name__ == "__main__":
    app.run(debug=True)
