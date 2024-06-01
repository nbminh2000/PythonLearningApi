from flask import Flask
from app.user import db
from app.user_controller import user_api

app = Flask(__name__)
app.register_blueprint(user_api, url_prefix='/api')

# Cấu hình cơ sở dữ liệu
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlserver://MSI\SQLEXPRESS:1434'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)

#commit on main branch