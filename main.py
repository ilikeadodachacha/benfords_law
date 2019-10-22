import os
from flask import Flask, render_template, request, redirect

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/", methods=['GET','POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")

  if request.method == 'POST':
    target = os.path.join(APP_ROOT, 'uploads/')
    print(target)

    for file in request.files.getlist("file"):
      print(file)
      filename = file.filename
      destination = "/".join([target, filename])
      print(destination)
      readfile = file.read()
      filearray = readfile.split('\n')
      print(filearray)
      # file.save(destination) 

    return render_template("home.html")

if __name__ == "__main__":
  app.run(debug=True)