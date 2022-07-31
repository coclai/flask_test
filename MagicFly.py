from flask import Flask, render_template, views, url_for
# import sqlHelper
from dbHelper import db

app = Flask(__name__)
app.config.from_object('config.settings.Config')
print(app.config['DB_HOST'])

DATA_DIC = {
    1: {'name': '张三', 'age': 18},
    2: {'name': '李四', 'age': 25},
}


# 自定义CBV视图的装饰器
def auth(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result

    return wrapper


class NewsView(views.MethodView):
    # methods = ['POST']  # 只允许POST请求
    decorators = [auth, ]  # 给请求加装饰器

    # get请求执行的代码
    def get(self):
        v = url_for('news')
        return 'get'

    # post请求执行的代码
    def post(self):
        return 'post'


# cbv
app.add_url_rule('/news', view_func=NewsView.as_view(name='news'))


class HelloView(views.View):
    methods = ['GET']

    def dispatch_request(self, name):
        return "Hello %s!" % name


app.add_url_rule('/hello/<name>', view_func=HelloView.as_view('hello'))


@app.route('/login')
def login():
    result = db.fetchOne('select * from web_models_admininfo where username = %s and password = %s', 'fanta',
                         '1551')
    # result = sqlHelper.fetchOne('select * from web_models_admininfo where username = %s and password = %s', 'fanta',
    #                             '1551')
    print(result)
    return "login"


@app.route("/index")
def index():
    data_dict = DATA_DIC
    return render_template('index.html', data_dict=data_dict)


@app.route("/order")
def order():
    return "order"


if __name__ == '__main__':
    app.run(debug=True)
