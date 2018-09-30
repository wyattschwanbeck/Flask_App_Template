from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from .Form_Declarations import LoginForm, RegisterForm, ChangePasswordForm, Alert

from flask_sqlalchemy  import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
csrf = CSRFProtect()
csrf.init_app(app)
app.config['SECRET_KEY'] = 'This should be a secret key that only you know!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dir/of/project_database'

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

bootstrap = Bootstrap(app)

project_name="Project Name"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html', project_name=project_name, user=current_user)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    alert = Alert()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return redirect(url_for('dashboard'))

        alert = Alert('danger', 'Username or password incorrect')
        #return '<h1>' + form.username.data + ' ' + form.password.data + '</h1>'

    return render_template('login.html', form=form, user=current_user, project_name=project_name, active_page='login', alert=alert)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    alert = Alert()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        check_username = User.query.filter_by(username=form.username.data).first()
        check_email = User.query.filter_by(email=form.email.data).first()
        if check_username:
            alert = Alert('danger', 'Username already exists')
        elif check_email:
            alert = Alert('danger', 'Email already exists with another username')
        else:
            new_user = User(username=form.username.data, email=form.email.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            user = User.query.filter_by(username=form.username.data).first()
            login_user(user)
            return redirect(url_for('dashboard'))
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form, user=current_user, alert=alert)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user, project_name=project_name)

@app.route('/settings', methods=['GET', 'POST'])
@login_required
def settings():
    user = User.query.filter_by(username=current_user.username).first()
    return render_template('settings.html', user=user, project_name=project_name)

@app.route('/settings/change_password', methods=['GET', 'POST'])
@login_required
def change_password():
    form = ChangePasswordForm()
    alert=Alert()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=current_user.username).first()
        if user:
            if form.new_password==form.retype_new_password:
                if check_password_hash(user.password, form.current_password.data):
                    hashed_password = generate_password_hash(form.retype_new_password.data, method='sha256')
                    user.password = hashed_password
                    alert = Alert("success", "Password Changed Successfully")
                    db.session.commit()
                else:
                    alert = Alert('danger', "Incorrect current password")
            else:
                alert = Alert('danger',"New Passwords did not match")
    return render_template('/settings/change_password.html', project_name=project_name, user=current_user, form=form, alert=alert)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
