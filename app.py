from flask import Flask, render_template, request, abort, redirect, url_for
import logging
import sys
from sfFunction import auth, getBalance, setNewExpCard, getLatestExpCard
import datetime

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for('formcallback'))

@app.route('/formcallback')
def formcallback():
    data = auth()
    print(data)
    print(data['records'][0]['Id'])
    print(data['records'][0]['Email'])
    return render_template('hello.html', dataInPage=data)
# ImmutableMultiDict([('company_name', 'hg'),
# ('company_site', 'sad'),
# ('first_name', 'asd'),
# ('last_name', 'g332'),
# ('birthday', '2021-05-08'),
# ('email', 'shpektras@gmail.com'),
# ('billing_country', 'sd'),
# ('billing_state', 'dqw'),
# ('billing_zip', 'fwq'),
# ('billing_city', 'wq'),
# ('billing_street', 'wqxqwxq')])

@app.route('/add-new-data', methods=['POST', 'GET'])
def add_new_data():
    if request.method == 'POST':
        print(request.form)
        return render_template('success.html')
    elif request.method == 'GET':
        return index()

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
