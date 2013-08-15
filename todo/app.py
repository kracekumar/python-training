from flask import Flask, render_template, url_for, abort, redirect, flash
import flask.ext.wtf as wtf
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('settings.py')
db = SQLAlchemy(app)


#### Forms ####
STATUS_CHOICES = [(0, "Pending"), (1, "Completed")]


class NewTodoForm(wtf.Form):
    title = wtf.TextField("Title", description="Name of the task", validators=[wtf.validators.Required()])
    status = wtf.SelectField("Task status", description="Current status of this task", coerce=int, choices=STATUS_CHOICES)


#### Models #####
class Task(db.Model):
    __tablename__ = "task"
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.Unicode(250), nullable=False)
    status = db.Column(db.Boolean, nullable=False, default=False)


@app.route("/")
def index():
    tasks = Task.query.all()
    return render_template("index.html", tasks=tasks)


@app.route("/new", methods=["GET", "POST"])
def new():
    form = NewTodoForm()
    if form.validate_on_submit():
        title = form.title.data
        status = form.status.data
        task = Task(title=title, status=status)
        db.session.add(task)
        db.session.commit()
        flash(u"%s added" % title, u"success")
        return redirect(url_for('index'))
    return render_template('new.html', form=form)


@app.route('/<title>')
def view_item(title):
    task = Task.query.filter_by(title=title).first()
    if task:
        return render_template('item.html', task=task)
    else:
        abort(404)


@app.route('/<title>/edit', methods=['POST', 'GET'])
def edit_item(title):
    task = Task.query.filter_by(title=title).first()
    if task:
        form = NewTodoForm(obj=task)
        if form.validate_on_submit():
            task.title = form.title.data
            task.status = form.status.data
            print task.status
            flash(u"%s edited" % title, u"success")
            db.session.commit()
            return redirect(url_for('index'))
        return render_template('new.html', form=form)


@app.route('/<title>/delete')
def delete_item(title):
    task = Task.query.filter_by(title=title).first()
    if task:
        db.session.delete(task)
        flash(u"%s deleted" % title, u"success")
        db.session.commit()
    return redirect(url_for('index'))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=5000)
