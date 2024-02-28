from flask import request, Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    name = request.args.get('name')
    message = request.args.get('message')
    return f'Hello {name}! {message}!'

if __name__ == '__main__':
    app.run()