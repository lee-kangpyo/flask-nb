from flask import Flask, render_template
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import MetaData

from flaskext.markdown import Markdown

# config.py 파일을 import
# import config


# 블루프린트 같은 다른 모듈에서 db 객체를 import 하기위해 전역으로 설정

naming_convention = {
    "ix": 'ix_%(column_0_label)s',
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s"
}

#db = SQLAlchemy()
#migrate = Migrate()

db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
migrate = Migrate()


def page_not_found(e):
    return render_template('404.html'), 404


def create_app():
    app = Flask(__name__)
    # app.config.from_object(config)  # config.py 파일을 플라스크 app 의 환경변수로 적용
    app.config.from_envvar('APP_CONFIG_FILE')
    # ORM(Object Relational Mapping)
    db.init_app(app)

    if app.config['SQLALCHEMY_DATABASE_URI'].startswith("sqlite"):
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

    # migrate 를 위한 model.py import
    from . import models

    # 블루프린트
    from .views import main_views, question_views, answer_views, auth_views, comment_view, vote_view
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    app.register_blueprint(auth_views.bp)
    app.register_blueprint(comment_view.bp)
    app.register_blueprint(vote_view.bp)

    # 템플릿 필터
    from .filter import format_datetime
    app.jinja_env.filters['datetime'] = format_datetime

    #Markdown
    Markdown(app, extentions=["nl2br", "fenced_code"])

    #오류 페이지 처리
    app.register_error_handler(404, page_not_found)

    return app
