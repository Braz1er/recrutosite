from flask import request, Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    return render_template('index.html', name='арвпрвра', message='fegefgssdf')

if __name__ == '__main__':
    app.run(debug=True)