from flask import Flask, render_template, request, redirect

app = Flask(__name__, static_url_path="", static_folder="static")
isLoggedIn = False
currentLogin = ""
userSkills = []
testSkills = []
adminSkills = []
passwordDic = {"user": "password","test": "test"}

@app.route('/')
def index():
    global isLoggedIn
    if isLoggedIn:
        return redirect('/profile')
    return render_template('login.html')

@app.route('/addSkill', methods=["POST"])
def addSkill():
    global skills
    global adminSkills 
    global userSkills
    global testSkills
    skill = request.form["skill"]
    if currentLogin == "admin":
        adminSkills.append(skill)
    if currentLogin == "user":
        userSkills.append(skill)
    if currentLogin == "test":
        testSkills.append(skill)
    return redirect('/profile')

@app.route('/login', methods=["POST"])
def login():
    global isLoggedIn, currentLogin, passwordDic
    userLogin = request.form["login"]
    userPass = request.form["password"]

    if userLogin in passwordDic and passwordDic[userLogin] == userPass:
        loginInner(userLogin, userPass)
        return redirect('/profile')
    else:
        error_message = "Duq mutqagrel eq sxal gaxtnabar"  
        return render_template("login.html", error_message=error_message)
                               
@app.route('/profile')
def profile():
    if not isLoggedIn:
        return redirect('/')
    else:
        skills=[]
        if currentLogin == 'user':
            skills = userSkills
        elif currentLogin == 'admin':
            skills = adminSkills
        elif currentLogin == 'test':
            skills = testSkills
            
    return render_template('profile.html', currentLogin=currentLogin, skills=skills)


@app.route('/signout', methods = ['POST'])
def signout():
    global isLoggedIn
    isLoggedIn = False
    return redirect('/')


@app.route('/signup', methods=['GET', 'POST'])  
def signup():
    global isLoggedIn, passwordDic, currentLogin
    
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        passwordDic[username] = password
        loginInner(username, password)
        return redirect('/profile')
    else:
        return render_template('signup.html')

def loginInner(login, password):
    global isLoggedIn, currentLogin
    isLoggedIn = True
    currentLogin = login

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    global isLoggedIn, passwordDic, currentLogin

    if not isLoggedIn:
        return redirect("/")

    error_message = None  

    if request.method == 'POST':
        current_password = request.form["currentPassword"]
        new_password = request.form["newPassword"]
        confirm_new_password = request.form["confirmNewPassword"]

        if currentLogin in passwordDic and passwordDic[currentLogin] == current_password:
            if new_password == confirm_new_password:
                passwordDic[currentLogin] = new_password
                return redirect('/profile')
            else:
                error_message = "Sxal e"
      
    return render_template('settings.html', error_message=error_message)


if __name__== '__main__':
    app.run(debug=True)
    

