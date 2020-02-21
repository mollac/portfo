from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

def write_to_file(data):
    with open('database.txt', mode='a', encoding='utf-8') as f:
        f.write(f"\n{data['email']},{data['subject']},{data['message']}")

def write_to_csv(data):
    with open('database.csv', mode='a', encoding='utf-8', newline ='') as f:
        csv_writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([data['email'], data['subject'], data['message']])
        

@app.route('/')
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'database error' 
    else:
        return('Something went rong, try again!')