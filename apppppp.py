from flask import request
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_recruto():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'Hello {name}! {message}!'

if __name__ == '__main__':
  app.run()