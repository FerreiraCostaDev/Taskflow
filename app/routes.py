from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from app import db
from app.models import User, Task

main = Blueprint('main', __name__)


# ── Auth ──────────────────────────────────────────────────────────────────────

@main.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('main.tasks'))
    return redirect(url_for('main.login'))


@main.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.tasks'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        confirm = request.form.get('confirm_password', '')

        if not all([username, email, password, confirm]):
            flash('Preencha todos os campos.', 'danger')
            return render_template('register.html')

        if password != confirm:
            flash('As senhas não coincidem.', 'danger')
            return render_template('register.html')

        if User.query.filter_by(username=username).first():
            flash('Nome de usuário já existe.', 'danger')
            return render_template('register.html')

        if User.query.filter_by(email=email).first():
            flash('E-mail já cadastrado.', 'danger')
            return render_template('register.html')

        user = User(username=username, email=email)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()

        flash('Conta criada com sucesso! Faça login.', 'success')
        return redirect(url_for('main.login'))

    return render_template('register.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.tasks'))

    if request.method == 'POST':
        email = request.form.get('email', '').strip()
        password = request.form.get('password', '')
        remember = request.form.get('remember') == 'on'

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user, remember=remember)
            next_page = request.args.get('next')
            return redirect(next_page or url_for('main.tasks'))

        flash('E-mail ou senha incorretos.', 'danger')

    return render_template('login.html')


@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Você saiu da conta.', 'info')
    return redirect(url_for('main.login'))


# ── Tasks ─────────────────────────────────────────────────────────────────────

@main.route('/tasks')
@login_required
def tasks():
    filter_status = request.args.get('status', 'all')
    filter_priority = request.args.get('priority', 'all')

    query = Task.query.filter_by(user_id=current_user.id)

    if filter_status == 'pending':
        query = query.filter_by(completed=False)
    elif filter_status == 'done':
        query = query.filter_by(completed=True)

    if filter_priority in ('baixa', 'media', 'alta'):
        query = query.filter_by(priority=filter_priority)

    all_tasks = query.order_by(Task.created_at.desc()).all()

    total = Task.query.filter_by(user_id=current_user.id).count()
    done = Task.query.filter_by(user_id=current_user.id, completed=True).count()
    pending = total - done

    return render_template(
        'tasks.html',
        tasks=all_tasks,
        total=total,
        done=done,
        pending=pending,
        filter_status=filter_status,
        filter_priority=filter_priority,
    )


@main.route('/tasks/new', methods=['POST'])
@login_required
def new_task():
    title = request.form.get('title', '').strip()
    description = request.form.get('description', '').strip()
    priority = request.form.get('priority', 'media')

    if not title:
        flash('O título da tarefa é obrigatório.', 'danger')
        return redirect(url_for('main.tasks'))

    task = Task(title=title, description=description, priority=priority, user_id=current_user.id)
    db.session.add(task)
    db.session.commit()
    flash('Tarefa criada!', 'success')
    return redirect(url_for('main.tasks'))


@main.route('/tasks/<int:task_id>/toggle', methods=['POST'])
@login_required
def toggle_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    task.completed = not task.completed
    db.session.commit()
    return redirect(url_for('main.tasks'))


@main.route('/tasks/<int:task_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()

    if request.method == 'POST':
        title = request.form.get('title', '').strip()
        if not title:
            flash('O título é obrigatório.', 'danger')
            return render_template('edit_task.html', task=task)

        task.title = title
        task.description = request.form.get('description', '').strip()
        task.priority = request.form.get('priority', 'media')
        db.session.commit()
        flash('Tarefa atualizada!', 'success')
        return redirect(url_for('main.tasks'))

    return render_template('edit_task.html', task=task)


@main.route('/tasks/<int:task_id>/delete', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.filter_by(id=task_id, user_id=current_user.id).first_or_404()
    db.session.delete(task)
    db.session.commit()
    flash('Tarefa removida.', 'info')
    return redirect(url_for('main.tasks'))
