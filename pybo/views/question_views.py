# question_views.py : Question Views

from flask import Blueprint, render_template, request, url_for
from werkzeug.utils import redirect
from pybo.models import Question
from pybo.forms import QuestionForm, AnswerForm
from pybo import db
from datetime import datetime

bp = Blueprint('question', __name__, url_prefix='/question')

@bp.route('/list/')
def _list() :
    page = request.args.get('page', type=int, default=1)  # 페이지
    question_list = Question.query.order_by(Question.create_date.desc())
    question_list = question_list.paginate(page=page, per_page=10)
    return render_template('question/question_list.html', question_list = question_list)

# http://127.0.0.1:5000/detail/2
@bp.route('detail/<int:question_id>/')
def detail(question_id) :
    # question = 'select * from Question where id = question_id'
    # question = Question.query.get(question_id)
    form = AnswerForm()
    question = Question.query.get_or_404(question_id)
    return render_template('question/question_detail.html', question=question, form=form)

@bp.route('/create/', methods=('GET', 'POST'))
def create() :
    form = QuestionForm()
    if request.method == 'POST' and form.validate_on_submit() :
        question = Question(subject=form.subject.data, content=form.content.data, create_date=datetime.now())
        db.session.add(question)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('question/question_form.html', form=form)