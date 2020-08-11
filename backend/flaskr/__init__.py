import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10
def get_paginated_questions(request, selection):
    page = request.args.get('page', 1, type=int)

    if page < 1:
        return abort(422)

    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE
    formatted_questions = [question.format()
                           for question in selection]

    return formatted_questions[start:end]
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  cors = CORS(app, resources={r"/*": {"origin": "*"}})
  
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods',
                          'GET, PATCH, POST, DELETE, OPTIONS')
    return response
 
  @app.route('/categories')
  def categories():
    categories = Category.query.all()
    categories_dict = {}
    for category in categories:
        categories_dict[category.id] = category.type

    return jsonify({
        'success': True,
        'categories': categories_dict
    }), 200
  @app.route('/categories/<int:id>/questions', methods=['GET'])
  def get_questions_by_category(id):
    category = Category.query.filter_by(id=str(id)).one_or_none()

    if (category is None):
        abort(422)

    questions = Question.query.filter_by(category=str(id)).all()

    paginated_questions = get_paginated_questions(request, questions)

    return jsonify({
        'success': True,
        'questions': paginated_questions,
        'total_questions': len(questions),
        'current_category': category.type
    })
  @app.route('/questions')
  def questions():
    questions = Question.query.order_by(Question.id).all()
    total_questions = len(questions)
    categories = Category.query.order_by(Category.id).all()
    current_questions = get_paginated_questions(request, questions)
    if (len(current_questions) == 0):
        abort(404)

    categories_dict = {}
    for category in categories:
        categories_dict[category.id] = category.type

    return jsonify({
        'success': True,
        'total_questions': total_questions,
        'categories': categories_dict,
        'questions': current_questions
    }), 200
    

  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question = Question.query.filter(Question.id == str(question_id)).one_or_none()
    if question == None:
      return abort(404)
    question.delete()
    return jsonify({
      "success": True,
      "deleted": question_id
    })

  @app.route('/questions', methods=['POST'])
  def add_question():
    body = request.get_json()

    if 'search_term' in body.keys():
        return find_questions(request, body['search_term'])

    question = Question(
        question=body['question'],
        answer=body['answer'],
        difficulty=body['difficulty'],
        category=body['category'],
    )
    question.insert()

    return jsonify({
        "success": True,
        "created": question.format()
    })

  def find_questions(request, search_term):
    questions = Question.query.filter(Question.question.ilike('%'+search_term+'%')).all()
    paginated_questions = get_paginated_questions(request, questions)

    if len(questions) > 0 and len(paginated_questions) < 1:
        return abort(404)

    return jsonify({
        "success": True,
        "questions": paginated_questions,
        "total_questions": len(questions),
        "current_category": None
    })

  @app.route('/quizzes', methods=['POST'])
  def get_guesses():
    r_json = request.get_json()
    
    answerd_questions = r_json['previous_questions']
    category = r_json['quiz_category']
    if ((category is None) or (answerd_questions is None)):
        abort(400)

    if (category['id'] > 0):
        questions = Question.query.filter_by(category=str(category['id'])).all()
    else:
        questions = Question.query.all()

    new_question = questions[random.randint(0, len(questions)-1)]
    not_answerd=True
    while not_answerd:
      if new_question.id in answerd_questions:
          new_question = questions[random.randint(0, len(questions)-1)]
      else:
          not_answerd = False

    return jsonify({
        'success': True,
        'question': new_question.format(),
    }), 200
  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Resource not found"
    }), 404

  @app.errorhandler(422)
  def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "Unprocessable request"
    }), 422

  @app.errorhandler(500)
  def server_error(error):
    return jsonify({
        "success": False,
        "error": 500,
        "message": "Server error"
    }), 500
  
  return app

    