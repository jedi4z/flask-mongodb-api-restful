from wtforms import Form, StringField, validators


class UserForm(Form):
    first_name = StringField('first name', [validators.DataRequired()])
    last_name = StringField('last name', [validators.DataRequired()])