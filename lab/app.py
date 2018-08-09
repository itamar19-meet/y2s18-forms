from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/',)
def home():
    return render_template('home.html',students = query_all())
    

@app.route('/add', methods=['GET', 'POST'])
def add_student_route():
    if(request.method == 'GET'):
        return render_template("add.html")
    else:                                                          
        n = request.form['name']
        y = request.form['year']
        f_l = request.form['finish_lab']
        add_student(n , y , f_l)
        print('reived post request')
        return render_template("add.html")




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
        
    return render_template('delete.html')
    query_all()





app.run(debug=True)


