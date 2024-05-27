from flask import Flask, render_template,request,redirect
import csv

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/works.html")
def works():
    return render_template("works.html")

@app.route("/<string:page_name>")
def index(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.csv',mode='a') as database2:
        email=data["email"]
        subject=data["subject"]
        message=data["message"]
        csv_writer=csv.writer(database2,delimiter=',',quotechar=';',quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email,message,subject])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method=="POST":
        data= request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return "something went wrong. Try again"



if __name__ == "__main__":
    app.run(debug=True)

