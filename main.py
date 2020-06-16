from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect
import forms
import configparser

config = configparser.RawConfigParser()
config.read('ConfigFile.properties')
{}
secret_key = config['SecretKey']['secret_key']

app = Flask(__name__)
app.secret_key = secret_key
csrf = CsrfProtect(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    title = 'Curso de Flask'
    comment_form = forms.CommentForm(request.form)

    if request.method == 'POST' and comment_form.validate():
        print(f'{comment_form.user.data}')
        print(f'{comment_form.email.data}')
        print(f'{comment_form.comment.data}')
    else:
        print('Error in the form')

    return render_template('index.html', title=title, form=comment_form)

if __name__ == '__main__':
    app.run(debug=True, port=3000, host='0.0.0.0')