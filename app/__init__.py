from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Instanciar o banco de dados
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configurações da aplicação
    app.config.from_object('app.config.Config')

    # Inicializar a extensão SQLAlchemy
    db.init_app(app)

    # Inicializar Flask-Migrate
    migrate = Migrate(app, db)

    # Registrar rotas
    from app.routes import car_bp
    app.register_blueprint(car_bp)

    return app
