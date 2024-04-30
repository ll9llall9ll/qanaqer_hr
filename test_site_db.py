from flask import Flask, render_template, request, redirect
import psycopg2

class User:
    def __init__(self, password, login, skills):
        self.login = login
        self.password = password
        self.skills = skills

app = Flask(__name__, static_url_path='', static_folder='static')

db_params = {
    'dbname': 'qanaqer_hr',
    'user': 'postgres',
    'password': 'postgres',
    'host': 'localhost',
    'port': '5432'
}

def insertData(q):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(q)
            connection.commit()

def selectData(q):
    with psycopg2.connect(**db_params) as connection:
        with connection.cursor() as cursor:
            cursor.execute(q)
            return cursor.fetchall()


currentUser = None
userDic = { 'admin': User('admin', 'admin', []), 'test': User('test', 'test', []) }

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    global currentUser
    global userDic
    login = request.form['login']
    password = request.form['password']

    if login in userDic and userDic[login].password == password:
        currentUser = User(login, password, [])
        ("SELECT * FROM users WHERE username = 'login' AND password = 'password'")

        return redirect('/profile')
    else:
        return render_template("login.html", error_message="Duq mutqagrel eq sxal gaxtnabar kam nman account arka che")

@app.route('/profile')
def profile():
    global currentUser

    if currentUser is None:
        return redirect('/')
    else:
        return render_template('profile.html', login=currentUser.login, skills=currentUser.skills)


@app.route('/signout', methods=['POST'])
def signout():
    global currentUser
    currentUser = None
    return redirect('/')

@app.route('/signup', methods=['POST', 'GET'])
def signup():
    global userDic, currentUser 

    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        if username in userDic:            
            return render_template("signup.html", error_message="Username already in use")
        else:
            insertData ("INSERT INTO users(username, password) VALUES('" + username + "', '" + password + "')")
            newUser = User(username, password, [])  
            userDic[username] = newUser
            currentUser = newUser
            return redirect('/profile')
    else:
        return render_template('signup.html')

if __name__ == '__main__': 
    app.run()