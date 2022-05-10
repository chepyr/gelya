import os
from flask import Flask, render_template

app = Flask(__name__)

LINKS_LIST = [
    ['deposit', 'Банковский вклад'],
    ['stocks', 'Акции']
]


@app.route('/')
def main():
    return render_template('main.html', links_list=LINKS_LIST)


@app.route('/deposit')
def deposit():
    return render_template('deposit.html', links_list=LINKS_LIST)


@app.route('/stocks')
def stocks():
    return render_template('stocks.html', links_list=LINKS_LIST)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
