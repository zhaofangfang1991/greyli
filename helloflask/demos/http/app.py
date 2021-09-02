from flask import Flask,request,abort,session,redirect,url_for,render_template
from jinja2.utils import generate_lorem_ipsum
app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name', 'zff')
    result = ''
    if 'logged_id' in session:
        result += '当前已登录'
    else:
        result += '未登录'
    return '<h1>hello, %s.这里是首页! %s</h1>' % (name, result) # 有安全漏洞。避免直接将用户传入的数据直接作为响应返回

# int转换器
@app.route('/goback/<any(red,blue):year>')
def go_back(year):
    return '用了any，好像也没有什么用啊, %s' %year

@app.before_request
def hook():
    1==2


# 使用abort手动抛出错误
@app.route('/888')
def funtion888():
    abort(404)


# session
import os
app.secret_key = os.getenv('SECRET_KEY', '123456')

@app.route('/secret')
def show_secret():
    return app.secret_key

# 模拟用户登录
@app.route('/login')
def login():
    session['logged_id'] = True
    return redirect(url_for('hello'))


# 模拟用户登录后，才能访问的后台
@app.route('/admin')
def admin():
    if 'logged_id' not in session:
        abort(403)
    return 'welcome, dear admin'


# 学习重定向
@app.route('/foo')
def foo():
    return 'Here is foo! Redirect to  <a href="%s">do something</a>' %url_for('do_something')

@app.route('/bar')
def bar():
    return 'Here is bar! Redirect to  <a href="%s">do something</a>' %url_for('do_something', next=request.full_path)

@app.route('/do_something')
def do_something():
    a = 1+2 # 这里可以登录
    # return redirect(url_for('index'))

    # 让请求回到上一次的url的两种方式
    # 1 利用referrer
    # return redirect(request.referrer or url_for('index'))
    # 2 利用查询参数
    # 第一步：在上一次请求，比如bar中加入当前页面URL的查询参数
    # 第二步：获取next的值，重定向过去
    # return redirect(request.args.get('next', url_for('index')))

    # 3 调用定义好的通用的重定向函数
    return redirect_back()

@app.route('/index')
def index():
    return 'Here is index page!'

# 定义一个通用的重定向回上一个页面的函数
def redirect_back(default='hello', **kwargs):
    for target in request.args.get('next'), request.referrer:
        if target:
            return redirect(target)
    return redirect(url_for(default, **kwargs))




# 点击“more”,利用Ajax获取更多文章信息

# AJAX
@app.route('/post')
def show_post():
    post_body = generate_lorem_ipsum(n=2)
    return render_template('post.html', post=post_body)


@app.route('/more')
def more():
    return generate_lorem_ipsum(2)

