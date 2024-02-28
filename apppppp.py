from flask import request, Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_recruto():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('index.html', name=name, message=message)