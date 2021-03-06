# Full Stack API Final Project

## Full Stack Trivia

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a  webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out. 

That's where you come in! Help them finish the trivia app so they can start holding trivia and seeing who's the most knowledgeable of the bunch. The application must:

1) Display questions - both all questions and by category. Questions should show the question, category and difficulty rating by default and can show/hide the answer. 
2) Delete questions.
3) Add questions and require that they include question and answer text.
4) Search for questions based on a text query string.
5) Play the quiz game, randomizing either all questions or within a specific category. 

Completing this trivia app will give you the ability to structure plan, implement, and test an API - skills essential for enabling your future applications to communicate with others. 

## Tasks

There are `TODO` comments throughout project. Start by reading the READMEs in:

1. [`./frontend/`](./frontend/README.md)
2. [`./backend/`](./backend/README.md)

We recommend following the instructions in those files in order. This order will look familiar from our prior work in the course.

## Starting and Submitting the Project

[Fork](https://help.github.com/en/articles/fork-a-repo) the [project repository]() and [Clone](https://help.github.com/en/articles/cloning-a-repository) your forked repository to your machine. Work on the project locally and make sure to push all your changes to the remote repository before submitting the link to your repository in the Classroom. 

## About the Stack

We started the full stack application for you. It is desiged with some key functional areas:

### Backend

The `./backend` directory contains a partially completed Flask and SQLAlchemy server. You will work primarily in app.py to define your endpoints and can reference models.py for DB and SQLAlchemy setup. 

### Frontend

The `./frontend` directory contains a complete React frontend to consume the data from the Flask server. You will need to update the endpoints after you define them in the backend. Those areas are marked with TODO and can be searched for expediency. 

Pay special attention to what data the frontend is expecting from each API response to help guide how you format your API. 

[View the README.md within ./frontend for more details.](./frontend/README.md)

### API Documentation

Base URI: http://127.0.0.1:5000/ + EndPoint

Available resources:

###### Error types you may face

* 400 – bad request:
 the server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing).
* 404 – resource not found: 
   Check the url.
* 422 – unprocessable:
   this error condition may occur if an json
   request body contains well-formed (i.e., syntactically correct), but
   semantically erroneous, json instructions.
* 500 – internal server error:
   There are some troubles with the website.

###### Categories: 
   * To get all categories:
     Base URI + categories  Method=GET
     ```json
      {
        "categories": {
            "1": "Science", 
            "2": "Art", 
            "3": "Geography", 
            "4": "History", 
            "5": "Entertainment", 
            "6": "Sports"
        }, 
        "success": true
      }

     ```
   * To get question related to specific categ
      Base URI + categories/<int:id\>/questions  Method=GET
     ```json
      {
        "current_category": "category4",
        "questions": [
          {
            "answer": "Cairo",
            "category": 4,
            "difficulty": 2,
            "id": 15,
            "question": "What is the capital of Egypt?"
          },
          {
            "answer": "Marrakesh",
            "category": 4,
            "difficulty": 2,
            "id": 15,
            "question": "What is the capital of Morocco?"
          }
        ],
        "success": true,
        "total_questions": 3
      }

     ```
###### Questions
   * To get all questions:
     Base URI + questions  Method=GET
     ```json
      {
        "categories": {
            "1": "Science",
            "2": "Art",
            "3": "Geography",
            "4": "History",
            "5": "Entertainment",
            "6": "Sports"
        },
        "questions": [
            
            {
                "answer": "Cairo",
                "category": 4,
                "difficulty": 2,
                "id": 12,
                "question": "What is the capital of Egypt?"
            },
            {
                "answer": "Lake Victoria",
                "category": 3,
                "difficulty": 2,
                "id": 13,
                "question": "What is the largest lake in Africa?"
            },
            {
                "answer": "1.216 Billion",
                "category": 3,
                "difficulty": 3,
                "id": 14,
                "question": "How many people are there in Africa?"
            },
            {
                "answer": "Marrakesh",
                "category": 4,
                "difficulty": 2,
                "id": 15,
                "question": "What is the capital of Morocco?"
            }
        ],
        "success": true,
        "total_questions": 4
      }
      ```
   * To delete question
      Base URI + questions/<int:id\>  Method=DELETE
     ```json
      {
        "success": "True",
        "message": "Question successfully deleted"
      }

     ```
   * To add new question 

    - Example: Base URL + questions -X POST -H "Content-Type: application/json" -d '
      ```json
      {
        "question": "What is Egypt famouse with?",
        "answer": "Pyramids",
        "difficulty": 3,
        "category": "6"
      }
      
      ```'
      
   * To search for a question 

    - Example: Base URL + questions -X POST -H "Content-Type: application/json" -d {"searchTerm": "capital"}'
      ```json
      {
        "questions": [
          {
            "answer": "Cairo",
            "category": 4,
            "difficulty": 2,
            "id": 15,
            "question": "What is the capital of Egypt?"
          },
          {
            "answer": "Marrakesh",
            "category": 4,
            "difficulty": 2,
            "id": 15,
            "question": "What is the capital of Morocco?"
          }
        ],
        "success": true,
        "total_questions": 20
      }
    ```
###### Quizes

      - Sample: Base URL + quizzes -X POST -H "Content-Type: application/json" -d {"previous_questions": [5, 9],"quiz_category": {"type": "History", "id": "4"}}

      ```json
      {
        "question": {
          "answer": "George Washington Carver",
          "category": 4,
          "difficulty": 2,
          "id": 12,
          "question": "Who invented Peanut Butter?"
        },
        "success": true
      }
      ```

    