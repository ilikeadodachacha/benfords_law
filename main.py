import os
from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route("/healthCheck")
def check():
  return "OK!"

@app.route("/", methods=['GET','POST'])
def home():
  if request.method == 'GET':
    return render_template("home.html")

  if request.method == 'POST':
    def IsInteger(s):
      try:
        int(s)
        return True
      except ValueError:
        return False
    numints = 0
    counts = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    for file in request.files.getlist("file"):
  
      readfile = file.read().decode("utf-8")
        
      readfile = readfile.split()

      for item in readfile:
        if IsInteger(item):
          firstdig = int(item[0])
          idx = firstdig - 1
          numints = numints + 1
          counts[idx] = counts[idx] + 1

  expected_dist = [0.30, 0.18, 0.12, 0.09, 0.08, 0.07, 0.06, 0.05, 0.04]
  actual_dist = list(map(lambda x: float(x / numints), counts))
    
  return render_template("home.html", expected=expected_dist, actual=actual_dist)

if __name__ == "__main__":
  app.run(host= '0.0.0.0')