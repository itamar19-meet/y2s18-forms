from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/',)
def home():
    
    ff = query_all()
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
        return render_template("add.html") , query_all()




@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))



@app.route('/delete', methods=['GET', 'POST'])
def delete_student():
    if(request.method == 'GET'):
        return render_template("delete.html")
    else:                                                          
        delete_id = request.form['student__id']
        
        delete_student_by_id(delete_id)
        print('reived post request')
        return render_template("delete.html")
    return render_template('delete.html')

app.run(debug=True)


