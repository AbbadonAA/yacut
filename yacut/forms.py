from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[
            DataRequired(message='Обязательное поле'),
            URL(message='Некорректная ссылка')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[
            Optional(),
            Length(1, 16),
            Regexp(
                regex=r'^[a-z_A-Z\d-]+\b',
                message='Допустимы только символы: a-Z, - , _ ')]
    )
    submit = SubmitField('Создать')
