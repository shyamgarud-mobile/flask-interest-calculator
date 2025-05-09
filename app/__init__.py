from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class='app.config.Config'):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)
    app.config.from_pyfile('config.py', silent=True)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints
    from app.controllers.loan_controller import loan_bp
    app.register_blueprint(loan_bp)
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    return app