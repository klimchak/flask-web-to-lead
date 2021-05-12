from flask import Flask, render_template, request, abort, redirect, url_for, flash
from simple_salesforce import Salesforce
from flask_recaptcha import ReCaptcha

# sf = Salesforce(username='webtoleadtask8@gmail.com', password='JfCx5UY55YHSxx7',
#                 security_token='pPbkhqsnhYo4j0YuPfrUBbwn')

app = Flask(__name__)
recaptcha = ReCaptcha(app=app)

app.config.update(dict(
    RECAPTCHA_ENABLED=True,
    RECAPTCHA_SITE_KEY="6Ldzl9AaAAAAACfwgifiSavC11hq0Wp_k8-EXdW-",
    RECAPTCHA_SECRET_KEY="6Ldzl9AaAAAAAOfokU2A6Jh173y6cQBAojvtXa-T",
))

recaptcha = ReCaptcha()
recaptcha.init_app(app)

app.config['SECRET_KEY'] = 'webtoleadtask8'


@app.route('/', methods=['POST', 'GET'])
def index(data):
    return redirect(url_for('formcallback'), data)


@app.route('/formcallback')
def formcallback(data):
    return render_template('hello.html', data=data)


# 6Ldzl9AaAAAAACfwgifiSavC11hq0Wp_k8-EXdW-
# 6Ldzl9AaAAAAAOfokU2A6Jh173y6cQBAojvtXa-T

@app.route('/add-new-data', methods=['POST', 'GET'])
def add_new_data():
    if request.method == 'POST':
        if recaptcha.verify():
            if 'add_shipping_address' in request.form:
                print('!!!!!!!  без галки !!!!!!!')
                data = True
                # data = sf.Lead.create({'Company': request.form['company_name'],
                #                        'Website': request.form['company_site'],
                #                        'FirstName': request.form['first_name'],
                #                        'LastName': request.form['last_name'],
                #                        'Birthdate__c': request.form['birthday'],
                #                        'Email': request.form['email'],
                #                        'Country': request.form['billing_country'],
                #                        'State': request.form['billing_state'],
                #                        'PostalCode': request.form['billing_zip'],
                #                        'City': request.form['billing_city'],
                #                        'Street': request.form['billing_street'],
                #                        'Add_shipping_address__c': True})
            else:
                print('!!!!!!!  без галки !!!!!!!')
                data = False
                # data = sf.Lead.create({'Company': request.form['company_name'],
                #                        'Website': request.form['company_site'],
                #                        'FirstName': request.form['first_name'],
                #                        'LastName': request.form['last_name'],
                #                        'Birthdate__c': request.form['birthday'],
                #                        'Email': request.form['email'],
                #                        'Country': request.form['billing_country'],
                #                        'State': request.form['billing_state'],
                #                        'PostalCode': request.form['billing_zip'],
                #                        'City': request.form['billing_city'],
                #                        'Street': request.form['billing_street'],
                #                        'Add_shipping_address__c': False})
            # if 'success' in data and data['success'] is True:
            if data is True:
                return render_template('success.html', data=request.form)
            else:
                # return render_template('hello.html', data=request.form)
                return index(request.form)
        else:
            flash('Error ReCaptcha')
            # return render_template('hello.html', data=request.form)  # ????
            return index(request.form)
    elif request.method == 'GET':
        return index()


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


if __name__ == '__main__':
    app.run()
