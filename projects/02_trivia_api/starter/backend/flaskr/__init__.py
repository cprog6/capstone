import os, random
from flask import Flask, request, abort, jsonify
from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.sql.sqltypes import String
from sqlalchemy.dialects import postgresql
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import json

from models import setup_db, session, Question, Category

QUESTIONS_PER_PAGE = 3

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO:
  Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)

  '''
  @TODO:
  Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type, Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PATCH, DELETE, OPTIONS')
    return response
    
  '''
  @TODO:
  Create an endpoint to handle GET requests for all available categories.
  '''
  @app.route('/categories', methods=['GET'])
  #@cross_origin
  def get_categories():

    cat_dict = {}
    categories = Category.query.order_by(Category.type).all()
    
    for category in categories:
      cat_dict[category.id] = category.type

    return jsonify({
      'success': True,
      'categories': cat_dict,
      })
   
  '''
  @TODO: Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  #@cross_origin
  def get_questions():
    # Implement pagniation
    page = request.args.get('page', 1, type=int)
    app.logger.warning('page: {}'.format(page))
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + 10
    start = 0
    end = 100


    current_category = request.args.get('current_category', 'Science', type=String)

    questions = session.query(Question).all()
    formatted_question = [question.format() for question in questions]
    app.logger.warning("totalFQ: {}".format(len(formatted_question)))

    cat_dict = {}
    categories = session.query(Category).all()
    for category in categories:
      cat_dict[category.id] = category.type
 
    return jsonify({
      'success': True,
      'questions':formatted_question[start:end],
      'total_questions':len(formatted_question),
      'categories': cat_dict,
      'currentCategory': current_category,
      'page': page
      })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 


  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  

  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 

  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions')
  #@cross_origin
  def get_questions_for_category(category_id):
    # Implement pagniation
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + 10

    current_category = request.args.get('current_category', '', type=String)

    app.logger.warning(current_category)
    questions = session.query(Question).filter_by(category = category_id).all()

    formatted_question = [question.format() for question in questions]
 
    return jsonify({
      'success': True,
      'questions':formatted_question[start:end],
      'totalQuestions':len(formatted_question),
      'currentCategory': current_category
      })
  
  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not.  @app.route('/questions', methods=['GET'])
  '''
  @app.route('/quiz')
  #@cross_origin
  def quiz():
    # Implement pagniation
    page = request.args.get('page', 1, type=int)
    app.logger.warning('page: {}'.format(page))
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + 10

    current_category = request.args.get('current_category', 'Science', type=String)

    questions = session.query(Question).all()
    formatted_question = [question.format() for question in questions]
    app.logger.warning("totalFQ: {}".format(len(formatted_question)))

    ##REWRITE like the formatted_question example
    cat_dict = {}
    categories = session.query(Category).all()
    for category in categories:
      cat_dict[category.id] = category.type

    prev_questions = [9]
    result = session.query(Question).join(Category).filter(Question.id.notin_(prev_questions)).filter(Category.type == 'Science')
    formatted_question = [question.format() for question in result]
    rand_question = random.choice(formatted_question)
    app.logger.warning("result: {}".format(formatted_question))
    app.logger.warning("result: {}".format(rand_question))  

    return jsonify({
      'success': True,
      'questions':formatted_question[start:end],
      'total_questions':len(formatted_question),
      'categories': cat_dict,
      'currentCategory': current_category,
      'page': page
      })



  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''

  return app