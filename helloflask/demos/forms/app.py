from flask import Flask,render_template,request,flash,redirect,url_for
import os
from forms import LoginForm

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'default_string')
app.config['WTF_I18N_ENABLED'] = False # 让flask-wtf使用wtforms内置的错误消息翻译

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# 1、在视图函数中实例化表单类LoginForm   2、在render_template()中使用关键字from将表单实例传入模板
'''
首先是实例化表单；如果是GET请求，就渲染模板；如果是POST请求，就调用validate()验证表单数据；
'''
@app.route('/basic', methods=['GET', 'POST'])
def basic():
    form = LoginForm()
    ''' 第一种写法
    if request.method == 'POST' and form.validate():
        pass # 获取表单数据并保存'''
    if form.validate_on_submit(): # 第二种写法
        # pass # 获取表单数据并保存
        username = form.username.data
        flash('欢迎你，%s' %username)
        return redirect(url_for('index'))
    return render_template('basic.html', form=form)

@app.route('/bootstrap')
def bootstrap():
    form = LoginForm()
    return render_template('bootstrap.html', form=form)





@app.route('/hong', methods=['POST', 'GET'])
def hong():
    form = LoginForm()
    if form.validate_on_submit():
        pass # 校验数据，并重定向
    return render_template('hong.html', form=form)