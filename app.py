from flask import Flask, render_template
import os
import models

# This method is run when "flask run" is run from the command line
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    
    # Load secret keys from instance/config.py file
    app.config.from_pyfile('config.py')

    # Tell flask what config file and class to load via .env variable in config.py
    app.config.from_object(os.environ['APP_SETTINGS'])

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    models.db.init_app(app)

    from models import User, Food

    with app.app_context():
        # models.db.drop_all()
        models.db.create_all()

    # if test_config is None:
    #     # load the instance config, if it exists, when not testing
    #     app.config.from_pyfile('config.py', silent=True)
    # else:
    #     # load the test config if passed in
    #     app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    import auth
    app.register_blueprint(auth.bp)

    import food
    app.register_blueprint(food.bp)

    return app