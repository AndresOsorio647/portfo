from flask import Flask, render_template,  url_for, request, redirect
import csv 
app = Flask(__name__)
print(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)


# @app.route("/templates/index.html")
# def index():
#    return render_template("index.html")


# @app.route("/templates/works.html")
# def works():
#    return render_template("works.html")


# @app.route("/templates/contact.html")
# def contact():
#    return render_template("contact.html")


# @app.route("/templates/components.html")
# def components():
#    return render_template("components.html")

# function that will save the data received in database.txt
def write_to_file (data):
    with open('database.txt', mode='a') as database:
        email= data["email"]
        subject= data["subject"]
        message= data["message"]
        file = database.write(f'\n{email},{subject},{message}')

# function that will save the data received in database.csv
def write_to_csv (data):
    with open('database.csv', newline='', mode='a') as database2:
        email= data["email"]
        subject= data["subject"]
        message= data["message"]
        csv_writer = csv.writer(database2, delimiter=',', quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,subject,message])


# function that connect the form with the server
@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect('/thankYou.html')
    else:
        return "something went wrong try again"
