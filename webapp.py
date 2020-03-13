from oege import *
from hash import *
from flask import Flask, request, send_from_directory, render_template, redirect

app = Flask(__name__)
conn = connect()
session = {}

@app.route('/')
def root():
    global session
    session = {}
    return render_template('index.html', title= None)

@app.route('/login', methods=['GET'])
def login():
    global session
    session = {}
    return render_template('login.html', title='Home')

@app.route('/login', methods=['POST'])
def user_login():
    global session
    #request.form zorgt ervoor dat je de data ophaalt die word ingevoerd in de html bestand
    userDetails = request.form
    print(userDetails)
    if userDetails['username'] and userDetails['password']:
        record = fetch_by_key_value("user","username",userDetails['username'],conn)
        if record and checkPassword(record['salt'],record['hash'],userDetails['password']):
            session = record
            print(session)
            return redirect('/patient')
    return render_template('login.html')


@app.route('/create', methods=['GET','POST'])
def create():
    global session
    if request.method == 'GET':
        session = {}
        return render_template('create.html', title='Home')
    else:
        userDetails = request.form
        if userDetails['username'] and userDetails['password']:
            record = {}
            record['id'] = None
            record['username'] = userDetails['username']
            record['salt'] = generateSalt()
            record['hash'] = calculateHash(record['salt'],userDetails['password'])
            store("user",record,conn)
            return redirect('/login')
        return render_template('create.html')

@app.route('/nurse', methods=['GET'])
def nurse():
    if session:
        nurse = fetch_by_id("nurse",1,conn)
        return render_template('nurse.html', title='Home', nurse=nurse)
    return redirect('/')

@app.route('/patient', methods=['GET'])
def patient():
    if session:
        return render_template('patient.html', title='Home')
    return redirect('/')

# route for other static files
@app.route('/<path:path>')
def send_files(path):
     return send_from_directory("./static/",path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
