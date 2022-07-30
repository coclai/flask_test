from flask import Flask, render_template
# import sqlHelper
from dbHelper import db

app = Flask(__name__)
app.config.from_object('config.settings.Config')
print(app.config['DB_HOST'])

DATA_DIC = {
    1: {'name': '张三', 'age': 18},
    2: {'name': '李四', 'age': 25},
}


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
