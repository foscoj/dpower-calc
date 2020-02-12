from flask import Flask
import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route("/upload")
def uploadCSV(self):
    file = request.files['file']
    data = pd.read_csv(file)
    print(data)

if __name__ == "__main__":
  app.run()
