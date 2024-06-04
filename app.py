from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def hello_world():  # put application's code here
    return render_template('index.html')


@app.route('/dev')
# @app.route('/')
def dev_community():  # put application's code here
    return render_template('dev_community.html')


@app.route('/gpt_generated')
def gpt_generated():  # put application's code here
    return render_template('gpt_generated.html')


@app.route('/patt_generated')
def patt_generated():  # put application's code here
    return render_template('patt_generated.html')


@app.route('/')
def git_r8():  # put application's code here
    return render_template('git_r8.html')


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8000, ssl_context=('cert.pem', 'key.pem'))


