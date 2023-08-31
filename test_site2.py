from flask import Flask, render_template, request, redirect

class User:
    def __init__(self, password, login, skills):
        self.login = login
        self.password = password
        self.skills = skills

app = Flask(__name__, static_url_path='', static_folder='static')

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
        currentUser = userDic[login]
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
    

@app.route('/addSkill', methods=['POST'])
def addSkill():
    global currentUser

    if currentUser is None:
        return redirect('/')

    skill = request.form['skill']
    currentUser.skills.append(skill)
    return redirect('/profile')

@app.route('/signout', methods=['POST'])
def signout():
    global currentUser
    currentUser = None
    return redirect('/')

@app.route('/signup', methods=['GET','POST'])
def signup():
    global userDic, currentUser  

    if request.method == 'POST':    
        username = request.form['username']
        password = request.form['password']
        if username in userDic:
            return render_template("signup.html", error_message="Username already in use")
        else:
            newUser = User(username, password, [])  
            userDic[username] = newUser
            currentUser = newUser
            return redirect('/profile')
    else:
        return render_template('signup.html')
    
def loginInner(login, password):
    global isLoggedIn, currentLogin
    isLoggedIn = True
    currentLogin = login

@app.route('/settings')
def getsettings():
    return render_template('settings.html')

    
@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global currentUser
    if currentUser is None:
        return redirect('/')

    error_message = None  

    if request.method == 'POST':
        current_password = request.form["currentPassword"]
        new_password = request.form["newPassword"]
        confirm_new_password = request.form["confirmNewPassword"]

        if currentUser.password == current_password:
            if new_password == confirm_new_password:
                if current_password != new_password: 
                    currentUser.password = new_password
                    return redirect('/profile')
                else:
                    error_message = "New password must be different from the current password"
            else:
                error_message = "Passwords do not match"
        else:
            error_message = "Current password is incorrect"
      
    return render_template('settings.html', error_message=error_message)


if __name__ == '__main__': 
    app.run()