from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()
from . import models # models에 있는 클래스가 migrate되기 위해서 필요한 라인이다.

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.jinja_env.line_statement_prefix = '#' # 장고에는 없는 jinja2를 사용하는 플라스크의 특징. 템플릿에서 '{%%}' 대신에 라인 맨 앞에 '#'만 붙이면 된다.

    db.init_app(app)
    migrate.init_app(app, db)

    # 블루프린터 설정
    from .views import main_views, question_views, answer_views, auth_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)

    # 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    return app