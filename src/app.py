from flask import Flask, render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
from flask_login import  LoginManager, login_user,logout_user,login_required, current_user
from flask_wtf.csrf import CSRFProtect
from config import config
app = Flask(__name__)

# MODELS
from models.ModelUser import ModelUser

# entities
from models.entities.User import User

mysql = MySQL(app)

login_manager_app = LoginManager(app)

csrf = CSRFProtect(app)

@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql,id)

@app.route('/', methods=['GET', 'POST'])
def index():    
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        user = User(0, username, email, password)
        ModelUser.register(mysql, user)
        flash('Registro exitoso. Ahora puedes iniciar sesión.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        username = 'text'
        user = User(0,username,email,password)

        logger_user = ModelUser.login(mysql,user)

        if logger_user:
            if logger_user.password:
                login_user(logger_user)
                return redirect(url_for('home'))
            else:
                flash('invalid password')
        else:
            flash('User not found...')
    else:
    #     if current_user.is_authenticated:
    #         print('AUTENTICADO CON SESION')
    #         print(current_user.username)
    #         print(current_user.get_id())
    #         return redirect(url_for('homo'))
        return render_template("login.html")
    
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Has cerrado sesión.', 'info')
    return redirect(url_for('login'))

@app.route('/home')
@login_required
def home():
    return render_template('home.html', usuario=current_user)

if __name__ == '__main__':
    csrf.init_app(app)
    app.config.from_object(config['dev'])
    app.run()