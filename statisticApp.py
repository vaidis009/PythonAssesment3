# vaidas siupienius
#assesment 3 upload file and generate statistics
# 17.01.2017

from flask import flask, render_template, request
import os


app = statiostic(__name__)
APP_ROOT= os.path.dirname(os.path.abspath(__file__))
@app.route("/")
def index():
    return render_template("uploadFile.html")
@app.route("/upload", method =['post'])
def upload():
    target = os.path.join(APP_ROOT, "filesUploded/")
    print(target)

if not os.path.isdir(target):
    os.mkdir(target)

for file in request.files.getlist('file'):
    print(file)
    filename=file.filename
    destination = "/".joint([target, filename])
    print(destionation)
    file.save(destination)
    
return render_template('complete.html')
if __name__ == __main__:
    app.run(port=4555, debug=True)
