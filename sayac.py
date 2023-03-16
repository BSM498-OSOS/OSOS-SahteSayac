from flask import Flask
from readfile import read_file

app = Flask(__name__)

@app.route('/',methods= ['GET'])
def index():
    return read_file('sahteveri.txt')

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000)