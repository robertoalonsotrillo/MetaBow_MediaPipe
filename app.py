import os
import pythoncode
import json
from flask_cors import CORS, cross_origin
from flask import Response, jsonify
from flask import Flask, request
from flask import render_template,redirect
from werkzeug.utils import secure_filename



app = Flask(__name__)
cors = CORS(app)
UPLOAD_FOLDER = path=os.path.join("static","uploads")
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/")
def home():
    if not (pythoncode.cap is None):
        pythoncode.cap.release()
    return render_template("index.html")

@app.route("/download")
def download():
    # if not (pythoncode.cap is None):
    #     pythoncode.cap.release()

    with open(pythoncode.filename, "r") as json_file:
        content = json.load(json_file)
        content=jsonify(content)
        content.headers['Content-Disposition']="attachment;filename={}".format(pythoncode.logfilename)
        return content

@app.route("/video_feed")
def video_feed():
    return Response(pythoncode.generate(),
                    mimetype="multipart/x-mixed-replace; boundary=frame")

@app.route("/video_feed_detection")
def video_feed_detection():
    pythoncode.detection()
    if not (pythoncode.cap is None):
        pythoncode.cap.release()
    return render_template("index.html")
                    
@app.route("/read")
@cross_origin()
def read():
    return render_template("var.json")

@app.route("/error")
def error():
    if not (pythoncode.cap is None):
        pythoncode.cap.release()
    return render_template("error.html")

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        data = request.form
        tempVideoInput=data["videoinput"]
        print(tempVideoInput)
        if tempVideoInput!="web-cam":
            if 'file' not in request.files:
                print("No File Given")
                return redirect('/error')
        file = request.files['file']
        if file.filename == '' and tempVideoInput!="web-cam":
            return redirect('/error')
        else:
            tempmodel=data["model"]
            templogFileName=data["log-file-name"]
            
            filename = "uploaded."+secure_filename(file.filename).split(".")[1] if tempVideoInput!="web-cam" else "none"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            pythoncode.updateVariable(tempmodel,tempVideoInput,filename,templogFileName)
            return render_template("index.html",filename=filename,modelInput=tempmodel,videoInput=tempVideoInput)

    if request.method == "GET":
        print("accessed via get")
        return redirect('/')

if __name__ == "__main__":
    pythoncode.app(app)