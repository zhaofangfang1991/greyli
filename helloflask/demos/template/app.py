from flask import Flask,render_template,flash,url_for,redirect
import os
app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'secret string')
user = {
    'username': 'Grey Li',
    'bio': 'A boy who loves movies and music.',
}

movies = [
    {'name': 'My Neighbor Totoro', 'year': '1988'},
    {'name': 'Three Colours trilogy', 'year': '1993'},
    {'name': 'Forrest Gump', 'year': '1994'},
    {'name': 'Perfect Blue', 'year': '1997'},
    {'name': 'The Matrix', 'year': '1999'},
    {'name': 'Memento', 'year': '2000'},
    {'name': 'The Bucket list', 'year': '2007'},
    {'name': 'Black Swan', 'year': '2010'},
    {'name': 'Gone Girl', 'year': '2014'},
    {'name': 'CoCo', 'year': '2017'},
]

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/watchlist')
def watchlist():
    return render_template('watchlist.html', user=user, movies=movies)


# 注册一个模板上下文处理函数
@app.context_processor
def inject_foo():
    foo = 'I am foo'
    return dict(foo=foo)

# 将函数注册为模板全局变量
@app.template_global()
def bar():
    return 'I am bar'


@app.route('/flash')
def just_flash():
    flash('I am flash, who is looking for me?')
    return redirect(url_for('index'))

# 自定义一个错误处理函数
@app.errorhandler(404)
def page_not_found(e):
    return render_template('errors/404.html'), 404

