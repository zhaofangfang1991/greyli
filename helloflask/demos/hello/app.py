import click
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>hello, world!</h1>'

@app.route('/greet', defaults={'name': '云迪娃'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>hello, %s, mummy is working hard. Are you growing up healthy?</h1>' % name

@app.route('/hello')
def hello():
    return 'hello world!'


# 定义一个flask命令
@app.cli.command('say_hello')
def say_hello():
    click.echo('hello,cli.command') # 此处是显示文字。也可以做其他的事情

'''
启动命令:
flask run --host=0.0.0.0 --port=8000
'''


