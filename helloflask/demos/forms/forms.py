from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms.validators import DataRequired,Length


# 定义一个LoginForm表单
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # <input type='text' name='Username' required>
    password = PasswordField('Password', validators=[DataRequired(), Length(8,128)]) # <input type='password' name='Password' required length=[8,128]>
    remember = BooleanField('Remember me') # <radio >