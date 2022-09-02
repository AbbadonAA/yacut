from flask import jsonify, request
import re

from . import app, db
from .models import URL_map
from .views import get_unique_short_id, check_short_id
from .constants import LINK_REG
from .error_handlers import APIErrors


@app.route('/api/id/', methods=['POST'])
def create_short_link():
    data = request.get_json()
    if not data:
        raise APIErrors('Отсутствует тело запроса')
    if 'url' not in data:
        raise APIErrors('\"url\" является обязательным полем!')
    if 'custom_id' in data:
        custom_id = data.get('custom_id')
        if not check_short_id(custom_id):
            raise APIErrors(f'Имя "{custom_id}" уже занято.')
        if custom_id == '' or custom_id is None:
            data['custom_id'] = get_unique_short_id()
        elif not re.match(LINK_REG, custom_id):
            raise APIErrors('Указано недопустимое имя для короткой ссылки')
    else:
        data['custom_id'] = get_unique_short_id()
    new_url = URL_map()
    new_url.from_dict(data)
    db.session.add(new_url)
    db.session.commit()
    return jsonify(new_url.to_dict()), 201


@app.route('/api/id/<short_id>/', methods=['GET'])
def get_original_url(short_id):
    original_url = URL_map.query.filter_by(short=short_id).first()
    if not original_url:
        raise APIErrors('Указанный id не найден', 404)
    return jsonify({'url': original_url.original}), 200
