from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin
import processor
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@cross_origin()
def index():
    return render_template('index.html')


@app.route('/word_count', methods=['GET', 'POST'])
@cross_origin()
def word_count():
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf8')) or {}
        text = processor.Text(data.get('text'))
        if data.get('order') == 'alpha':
            sort = text.sorted_wbc_alphabetically()
        elif data.get('order') == 'count':
            sort = text.sorted_wbc_by_count()
        else:
            sort = text.words_by_count
        html = '<br>' + '<br>'.join([str(i) + ':' + str(sort[i]) for i in sort])
        return jsonify({'res': html})
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
