import random

from flask import abort, flash, redirect, render_template

from . import app, db
from .constants import S_LENGTH, SYMBOLS
from .forms import URL_mapForm
from .models import URL_map


def check_short_id(short_id):
    """Проверка уникальности нового адреса."""
    if URL_map.query.filter_by(short=short_id).first() is None:
        return True
    return False


def get_unique_short_id():
    """Генерация случайной уникальной последовательности из 6 символов."""
    short_id = ''.join(random.choice(SYMBOLS) for i in range(S_LENGTH))
    if check_short_id(short_id):
        return short_id
    return get_unique_short_id()


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if not custom_id:
            custom_id = get_unique_short_id()
        elif not check_short_id(custom_id):
            flash(f'Имя {custom_id} уже занято!', 'link-taken')
            return render_template('index.html', form=form)
        new_url = URL_map(
            original=form.original_link.data,
            short=custom_id
        )
        db.session.add(new_url)
        db.session.commit()
        return render_template('index.html', url=new_url, form=form)
    return render_template('index.html', form=form)


@app.route('/<short_id>')
def follow_link(short_id):
    original_link = URL_map.query.filter_by(short=short_id).first()
    if not original_link:
        abort(404)
    return redirect(original_link.original)
