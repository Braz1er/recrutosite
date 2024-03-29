from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('index.html', n=name, m=message)

if __name__ == '__main__':
    app.run()