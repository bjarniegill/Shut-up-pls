import json
from flask import Flask, make_response, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    templateData = {}
    return render_template('index.html', **templateData)


@app.route('/api/action/')
def action():
    some_param = request.args.get('some param')
    data = {'success': True}

    return make_response(json.dumps(data), 200)


if __name__ == '__main__':
    app.run(debug=True, port=80, host='127.0.0.1')