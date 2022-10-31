from flask import flash, redirect, render_template

from . import app, db
from .forms import URL_mapForm
from .models import URL_map
from .utils import check_short_id, get_db_object, get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if not form.validate_on_submit():
        return render_template('main.html', form=form)
    custom_id = form.custom_id.data
    if not custom_id:
        custom_id = get_unique_short_id()
    elif not check_short_id(custom_id):
        flash(f'Имя {custom_id} уже занято!', 'link-taken')
        return render_template('main.html', form=form)
    new_url = URL_map(
        original=form.original_link.data,
        short=custom_id
    )
    db.session.add(new_url)
    db.session.commit()
    flash(f'{custom_id}')
    return render_template('main.html', url=new_url, form=form)


@app.route('/<short_id>')
def follow_link(short_id):
    db_object = get_db_object(URL_map.short, short_id).first_or_404()
    original_link = db_object.original
    return redirect(original_link)
