from flask import Flask, render_template, request, abort, redirect, url_for
import logging
import sfFunction

app = Flask(__name__)




@app.route('/', methods=['POST', 'GET'])
def index():
    return redirect(url_for('formcallback'))


@app.route('/formcallback')
def formcallback():
    # data = auth()
    # print(data)
    # print(data['records'][0]['Id'])
    # print(data['records'][0]['Email'])
    return render_template('hello.html')


@app.route('/add-new-data', methods=['POST', 'GET'])
def add_new_data():
    if request.method == 'POST':
        data = sfFunction.sf.Lead.create({'Company': request.form['company_name'],
                                          'Website': request.form['company_site'],
                                          'FirstName': request.form['first_name'],
                                          'LastName': request.form['last_name'],
                                          'Birthdate__c': request.form['birthday'],
                                          'Email': request.form['email'],
                                          'Country': request.form['billing_country'],
                                          'State': request.form['billing_state'],
                                          'PostalCode': request.form['billing_zip'],
                                          'City': request.form['billing_city'],
                                          'Street': request.form['billing_street']})

        if data['success'] == True:
            logging.info('\nЗапись создана\nДанные карты')
            logging.info(data)
        else:
            logging.info('\nЗапись НЕ создана\nДанные карты')
            logging.info(data)
        print(data)
        return render_template('success.html')
    elif request.method == 'GET':
        return index()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
