from datetime import datetime
from flask_login import logout_user, login_user, current_user, login_required, UserMixin
from final_pro import db, app, bcrypt, login_manager
from flask import url_for, redirect, render_template, flash, request, session
from sqlalchemy import or_


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_type = db.Column(db.String(200), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    zip_code = db.Column(db.String(200), nullable=False)
    password = db.Column(db.String(120), nullable=False)


class Insurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    company = db.Column(db.String(120), nullable=False)
    rate = db.Column(db.String(20), nullable=False)
    type = db.Column(db.String(20), nullable=True)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.png')


class UserInsurance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    insurance_id = db.Column(db.Integer)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())


class UserChat(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user1_id = db.Column(db.Integer)
    user2_id = db.Column(db.Integer)
    msg = db.Column(db.String(300), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.now())


from final_pro.forms import LoginForm, RegistrationForm


@app.route("/")
@app.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    all_insurance = Insurance.query.paginate(page=page, per_page=5)
    if session.get('search'):
        all_insurance = Insurance.query.filter(
            Insurance.name.contains(session.get('search'))
            | Insurance.company.contains(session.get('search'))
            | Insurance.description.contains(session.get('search'))
            | Insurance.type.contains(session.get('search'))) \
            .paginate(page=page, per_page=3)

    return render_template('index.html', title='Home', all_insurance=all_insurance)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@login_required
@app.route("/charts")
def charts():
    return render_template('chart.html', title='Charts')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data, user_type=form.user_type.data,
                    address=form.address.data, zip_code=form.zip_code.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your Account has been created, You can now login', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, title='Register')


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))

        flash('Unsuccessful login', 'danger')
    return render_template('login.html', form=form, title='Login')


@app.route("/insurance/<int:insurance_id>", methods=['GET', 'POST'])
@login_required
def view_insurance(insurance_id: int):
    insu = Insurance.query.get(insurance_id)
    if request.method == 'POST':
        usr_ins = UserInsurance(user_id=current_user.id, insurance_id=insu.id)
        db.session.add(usr_ins)
        db.session.commit()
        flash(f'Thanks for selecting {insu.name}', 'success')
        return redirect(url_for('user_insurance'))
    return render_template('view-ins.html', title='View Insurance', insu=insu)


@login_required
@app.route("/insurance/user")
def user_insurance():
    usr_ins = UserInsurance.query.filter_by(user_id=current_user.id).all()
    return render_template('user-ins.html', title='Insurance', usr_ins=usr_ins, Insurance=Insurance)


@login_required
@app.route("/insurance/all")
def all_insurance():
    if current_user.user_type != 'Admin':
        flash('Unauthorized User', 'danger')
        return redirect(url_for('home'))
    ins = Insurance.query.all()
    return render_template('all-ins.html', title='All Insurance', ins=ins)


@login_required
@app.route("/users/all")
def user_all():
    if current_user.user_type != 'Admin':
        flash('Unauthorized User', 'danger')
        return redirect(url_for('home'))
    users = User.query.all()
    return render_template('all-user.html', title='All Users', users=users)


@login_required
@app.route("/agent/chat", methods=['GET', 'POST'])
def agent_chat():
    chats = UserChat.query.filter(or_(UserChat.user1_id == current_user.id, UserChat.user2_id == current_user.id)) \
                      .order_by(UserChat.date_created.desc()).group_by(UserChat.user1_id).all()
    return render_template('chat-view.html', title='Chats', chats=chats, User=User)


@login_required
@app.route("/agent/<int:user_id>/chat", methods=['GET', 'POST'])
def agent_chat_view(user_id):
    chats = UserChat.query.filter(or_(UserChat.user1_id == user_id, UserChat.user2_id == user_id)).all()
    if request.method == 'POST':
        cht = UserChat(user2_id=user_id, user1_id=current_user.id, msg=request.form.get('msg'))
        db.session.add(cht)
        db.session.commit()
        return redirect(url_for('agent_chat_view', user_id=user_id))
    return render_template('chat.html', title='Chats', chats=chats)


@login_required
@app.route("/users/chat", methods=['GET', 'POST'])
def user_chat():
    chats = UserChat.query.filter(or_(UserChat.user1_id == current_user.id, UserChat.user2_id == current_user.id)).all()
    if request.method == 'POST':
        agent = User.query.filter_by(user_type='Agent').first()
        cht = UserChat(user1_id=current_user.id, user2_id=agent.id, msg=request.form.get('msg'))
        db.session.add(cht)
        db.session.commit()
        return redirect(url_for('user_chat'))
    return render_template('chat.html', title='Chats', chats=chats)


@login_required
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/search", methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        session['search'] = request.form.get('search')
        return redirect(url_for('home'))
    flash('Something went wrong please try again', 'info')
    return redirect(url_for('home'))
