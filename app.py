import re

from flask import (
    Flask,
    render_template,
    jsonify,
    request
)

from extractor import extract

URL_REGEX = re.compile(
    "([a-z]([a-z]|\d|\+|-|\.)*):(\/\/(((([a-z]|\d"
    "|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])"
    "|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:)*@)?((\[(|(v"
    "[\da-f]{1,}\.(([a-z]|\d|-|\.|_|~)|[!\$&'\(\)\*\+,;=]"
    "|:)+))\])|((\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\."
    "(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d"
    "|2[0-4]\d|25[0-5])\.(\d|[1-9]\d|1\d\d|2[0-4]\d|25[0-5]))"
    "|(([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])"
    "|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=])*)(:\d*)?)(\/(([a-z]|\d|-|\."
    "|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|"
    "[!\$&'\(\)\*\+,;=]|:|@)*)*|(\/((([a-z]|\d|-|\.|_|~|[\x00A0-"
    "\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)"
    "\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-"
    "\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)*)*)"
    "?)|((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])"
    "|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)+(\/(([a-z]|\d|-|\.|_|~|"
    "[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)"
    "\*\+,;=]|:|@)*)*)|((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF"
    "\xFDF0-\xFFEF])|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)){0})"
    "(\?((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])"
    "|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|[\xE000-\xF8FF]|\/|\?)*)?"
    "(\#((([a-z]|\d|-|\.|_|~|[\x00A0-\xD7FF\xF900-\xFDCF\xFDF0-\xFFEF])"
    "|(%[\da-f]{2})|[!\$&'\(\)\*\+,;=]|:|@)|\/|\?)*)?""")

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/extract')
def extract_url():
    url = request.args.get('url', '')
    if not URL_REGEX.match(url):
        return jsonify({
            'type': 'error',
            'message': 'Invalid URL'
        }), 406
    return jsonify(type='success', message=extract(url))

if __name__ == '__main__':
    app.run(debug=True, port=5000)
