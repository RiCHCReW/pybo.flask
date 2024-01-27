from flask import Blueprint, url_for
from werkzeug.utils import redirect

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/hello')
def hello_pybo():
  return 'Hello, Pybo!'


@bp.route('/')
def index():
  # url_for는 템플릿에서도 사용된다.
  return redirect(url_for('question._list')) # 'question._list'는 'question'이라는 이름을 갖는 블루프린트의 '_list'함수를 의미함.