from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    # add_student_route()
    print(query_all())
    return render_template('home.html')


@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
    if(request.method == 'GET'):
        return render_template("add.html")
    else:
        n = request.form['name']
        s = request.form['year']
        b = request.form['finish_lab']
        add_student(n , s , b)
        print('reived post request')
        return render_template("add.html")

@app.route('/student/<int:student_id>')
def display_student(student_id):

    return render_template('student.html', student=query_by_id(student_id))

app.run(debug=True)


