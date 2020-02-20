import os
import sys
import datetime
from flask import Flask, render_template, url_for, request, redirect
#from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
import json
from flask_cors import CORS
from werkzeug.utils import secure_filename

sys.path.append('lib/')
import import_excel

app = Flask(__name__)
# Flask-Cors
cors = CORS(app, resources={r"/*": {"origins": ["http://localhost*","http://thuyloibentre.com*"]}})

#######################################
#Function
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

###################################


UPLOAD_FOLDER = 'D:/sync/websvr/python/py_import_excel/upload/'
ALLOWED_EXTENSIONS = set(['xlsx', 'xls'])

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

#default
@app.route('/', methods = ['POST','GET'])
def blank():
	return ('hahahaa')


@app.route('/import/cctl_giatri_mucnuoc', methods=['GET', 'POST'])
def upload_cctl_giatri_mucnuoc():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            kq_temp=''
            kq_temp+='Tên file <p>{}</p>'
            kq_temp+='hahahaha <p>{}</p>'
            filename = secure_filename(file.filename)
            nowdatetime = datetime.datetime.now()
            filename='file'+nowdatetime.strftime("%d-%m-%Y_%Hh%Mm%S")+'-'+filename
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #imgurl=url_for('static',filename=filename)
            detect=UPLOAD_FOLDER+filename
            
            file_path='upload/'+filename
            err=import_excel.check_cctl_giatri_mucnuoc(file_path)

            #return kq_temp.format(filename,detect)
            return json.dumps(err)
    return '''
    <!doctype html>
    <title>Test upload excel</title>
    <h1>Test upload excel</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''


@app.route('/flower_detection', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            kq_temp=''
            kq_temp+='<table width="600px">'
            kq_temp+='<tr>'
            kq_temp+='<td width="300px" style="padding:20px;">'
            kq_temp+='<img src="{}" width="300px">'
            kq_temp+='</td>'
            kq_temp+='<td>'
            kq_temp+='<h2>Thông tin nhận dạng</h2>'
            kq_temp+='<p>{}</p>'
            kq_temp+='<br>'
            kq_temp+='<hr>'
            kq_temp+='<br>'
            kq_temp+='<a href="http://rose.dothanhlong.org:999/flower_detection">Nhận diện bông hoa (Deep learning testing)</a>'
            kq_temp+='</td>'
            
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #detect=detect_bonghoa("static/h1.jpg")
            #return detect_bonghoa("upload/h1.jpg")
            imgurl=url_for('static',filename=filename)
            detect=detect_bonghoa("static/"+filename)
            return kq_temp.format(imgurl,detect)
    return '''
    <!doctype html>
    <title>Nhận diện bông - soiqualang chentreu</title>
    <h1>Upload hình bông hoa</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

if __name__ == "__main__":
	app.run(debug=True)
	# app.run(host='10.10.10.4', port=5000, debug=False)

##http://127.0.0.1:5000/select?kind=stations&ingestion=20160101	
## 