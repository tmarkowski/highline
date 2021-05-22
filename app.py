from flask import Flask, render_template, redirect, url_for, request

import requests
from datetime import date

app = Flask (__name__)


artworkdict = [{
        "name": "Retainer",
        "artist": "Hannah Levy",
        "date":"April 2021 - March 2022",
        "medium": "Carved Marble and Stainless Steel",
        "description":"An oversized orthodontic retainer from carved marble and stainless steel, in conversation with the architecture and design of the park and its surroundings.",
        "questions":[{
            "question":"What is a retainer?",
            "answers":["A public bench to sit on","a orthadontic device to keep your teeth straight","A waterslide",
            "a torture device"],
            "correct_answer": 1
        },{
            "question":"What is this piece made of?",
            "answers":["Rubber and Popsicles","Ice","Stainless Steel and Marble",
            "Iron and Marble"],
            "correct_answer": 2
        },{
            "question":"What is the theme of this piece",
            "answers":["Crooked Teeth","Being at the Dentist","How giant retainers are better than small ones",
            "Social Class and Status"],
            "correct_answer": 3
        }
        ]
},{
        "name": "57 Forms of Liberty",
        "artist": "Ibrahim Mahama",
        "date":"April 2021 - March 2022",
        "medium": "industrial tank, tree",
        "description": "An inverted industrial tank with a tree sprouting from its' mouth",
         "questions":[{
            "question":"Where is the Industrial Tank from?",
            "answers":["the moon","Kansas","New York","North Carolina"],
            "correct_answer": 3
        },{
            "question":"Looking at the sculpture from a perspective looking North, what is behind the sculpture?",
            "answers":["Taj Mahal","Hudson Yards / The Edge","Another Industrial Tank","The Hudson River"],
            "correct_answer": 1
        },{
            "question":"What NYC tourist destination is the tree on top of the tank mirror?",
            "answers":["The Statue of Liberty","Effiel Tower","Empire State Building","Central Park"],
            "correct_answer": 0
        }
        ]
}
]




@app.route('/')
def index():
  return render_template('index.html')

@app.route('/quiz')
def quiz():
  return render_template('quiz.html', data=artworkdict)

@app.route('/gallery')
def gallery():
  return render_template('gallery.html')

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
