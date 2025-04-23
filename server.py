from flask import Flask, session, redirect, url_for
from flask import render_template
from flask import Response, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.urandom(24)

learning_page1_data= [
   {
      "id": "1",
      "theory": "monochrome",
      "content": ["Tints and tones of a single base color create a soft, refined color palette.",
                  "This approach offers a versatile and understated combination.",
                  "It's easy to apply in fashion.","Helps achieve a balanced, cohesive look."],
      "color_wheel": "https://images.akzonobel.com/akzonobel-flourish/dulux/ie/en/articles/colour-theory-made-easy/colourwheel-duluxuk-jpeg.jpg?impolicy=.auto&imwidth=1366",
      "comment_text": "Click to explore Orange as a base",
      "popup_text": "base color orange with 3 variances",
      "colors":["#f9cb9cff", "#f6b26bff", "#e69138ff"],
      "color_amount": "3",
      "next_lesson":"/learn/1b"
   },
   {
      "id": "2",
      "theory": "Complementary",
      "content":["Two colors positioned opposite each other on the color wheel create a bold, high-contrast pairing.",
                 "This combination enhances the vibrancy of both colors.", "It grabs attention and creates a visually striking effect when used together."],
      "color_wheel": "https://images.akzonobel.com/akzonobel-flourish/dulux/ie/en/articles/colour-theory-made-easy/colourwheel-duluxuk-jpeg.jpg?impolicy=.auto&imwidth=1366",
      "comment_text":"Click to explore red and its complement",
      "popup_text":"red and green as complementary colors",
      "colors":["#cc0000ff","#357c69ff"],
      "color_amount":"2",
      "next_lesson":"/learn/2b"
   },
   {
      "id": "3",
      "theory": "Triadic",
      "content":["Three colors evenly spaced around the color wheel form a triadic color scheme.","This scheme offers strong contrast, but is more balanced than complementary pairs.",
                 "It’s more adaptable for various styles and settings.", "The result is a bold, lively color palette with a dynamic yet harmonious feel."],
      "color_wheel": "https://images.akzonobel.com/akzonobel-flourish/dulux/ie/en/articles/colour-theory-made-easy/colourwheel-duluxuk-jpeg.jpg?impolicy=.auto&imwidth=1366",
      "comment_text":"Click to explore the rbg triadic",
      "popup_text":"Red, blue, and green of the same hue is the most basic triadic combination",
      "colors":["#be414bff","#4bbe41ff", "#414bbeff"],
      "color_amount":"3",
      "next_lesson":"/learn/3b"
   },
   {
      "id": "4",
      "theory": "Tetradic",
      "content":["Uses four evenly spaced colors on the color wheel to create a dynamic palette.","To maintain balance, it’s best to let one color take the lead.",
                 "The remaining colors should be used as accents.","With more colors involved, achieving harmony can be more challenging."],
      "color_wheel": "https://images.akzonobel.com/akzonobel-flourish/dulux/ie/en/articles/colour-theory-made-easy/colourwheel-duluxuk-jpeg.jpg?impolicy=.auto&imwidth=1366",
      "comment_text":"Click to explore the rbyg triadic",
      "popup_text":"Red, blue, yellow and green of the same hue is the most basic tetradic combination",
      "colors":["#d12e81ff","#d1cf2eff","#2ed17eff","#2e30d1ff"],
      "color_amount":"4",
      "next_lesson":"/learn/4b"
   }
]

learning_page2_data= [
   {
      "id": "1",
      "theory": "Monochrome",
      "content":["Monochromatic are easy on the eyes and effortlessly stylish.", "This approach simplifies dressing while maintaining a bold, put-together appearance.",
                 "Examples include all-blue, all-beige, or all-black outfits.","Depth and interest are added through variations in texture and tone."],
      "bases":["base:pink","base:gray"],
      "colors_1":["#e17083ff","#eab3bfff", "#f1d2d9ff"],
      "colors_2":["#303030ff","#666666ff","#d9d9d9ff"],
      "color_amount":"3",
      "outfit_1":"/static/monochrome_1.png",
      "outfit_2":"/static/monochrome_2.png",
      "next_lesson":"/learn/2a"
   },
   {
      "id": "2",
      "theory": "Complementary",
      "content":["Complementary color outfits use bold, opposing hues.","They create striking contrast, adding excitement and making each color stand out.",
                 "The result is an eye-catching, confident look.", "Examples include blue and yellow or pink and light green styled together."],
      "bases":["pink/light green","blue/yellow"],
      "colors_1":["#a5b4a5ff","#f1d2d9ff"],
      "colors_2":["#c9daf8ff","#fff2ccff"],
      "color_amount":"2",
      "outfit_1":"/static/complementary_1.png",
      "outfit_2":"/static/complementary_2.png",
      "next_lesson":"/learn/3a"
   },
   {
      "id": "3",
      "theory": "Triadic",
      "content":["Triadic color outfits use three evenly spaced hues on the color wheel.","They create bold, vibrant combinations with a balanced feel.",
                 "This approach brings energetic contrast while maintaining harmony.","Each color stands out without overwhelming the overall look.",
                 "Example: red, green, and blue styled in a fun, cohesive way."],
      "bases":["red/blue/green","light pink/light green/light blue"],
      "colors_1":["#980000ff","#274e13ff","#1c4587ff"],
      "colors_2":["#e39cc3ff","#c3e39cff","#9cc3e3ff"],
      "color_amount":"3",
      "outfit_1":"/static/triadic_1.png",
      "outfit_2":"/static/triatic_2.png",
      "next_lesson":"/learn/4a"
   },
   {
      "id": "4",
      "theory": "Tetradic",
      "content":[
         "Tetradic color outfits use four distinct hues spaced evenly on the color wheel.","Each color stands out while still contributing to a cohesive look.",
         "To maintain balance, one color could take the lead.", "The other three colors should be used as supporting accents.",
         "Example: combining red, green, blue, and yellow in a bold yet intentional way."],
      "bases":["red/blue/green/yellow","nyon red/blue/green/yellow"],
      "colors_1":["#980000ff","#274e13ff","#1c4587ff","#f1c232ff"],
      "colors_2":["#fac1efff","#fae8c1ff","#c1facbff","#c1d2faff"],
      "color_amount":"4",
      "outfit_1":"/static/tetradic_1.png",
      "outfit_2":"/static/tetradic_2.png",
      "next_lesson":"/quiz/1"
   }
]

# Define data for the quiz questions
quiz_data = [
    {
        "id": "1",
	"page_number": "1/4",
        "theme": "monochrome",
        "question_text": "PICK A TOP COLOR TO MAKE A MONOCHROME OUTFIT",
        "image_url": "/static/monochrome.png",
        "base_color": "#4a86e8",
        "options": [
            {"color": "#a4c2f4", "is_correct": True},
            {"color": "#e06666", "is_correct": False},
            {"color": "#b6d7a8", "is_correct": False},
            {"color": "#ffd966", "is_correct": False}
        ],
        "feedback_correct": "GREAT WORK",
        "feedback_incorrect": "NOT QUITE… TRY TO MAKE A MONOCHROME OUTFIT AGAIN!",
        "next_question": "/quiz/2"
    },
    {
        "id": "2",
	"page_number": "2/4",
        "theme": "triadic",
        "question_text": "PICK A SWEATER COLOR TO MAKE A TRIADIC OUTFIT",
        "image_url": "/static/triadic.png",
        "base_colors": ["#cc0000", "#1c4587"],
        "options": [
            {"color": "#e69138", "is_correct": False},
            {"color": "#274e13", "is_correct": True},
            {"color": "#674ea7", "is_correct": False},
            {"color": "#ffd966", "is_correct": False}
        ],
        "feedback_correct": "GREAT WORK",
        "feedback_incorrect": "NOT QUITE… TRY TO MAKE A TRIADIC OUTFIT AGAIN!",
        "next_question": "/quiz/3"
    },
    {
        "id": "3",
	"page_number": "3/4",
        "theme": "complementary",
        "question_text": "PICK A TOP COLOR TO MAKE A COMPLEMENTARY OUTFIT",
        "image_url": "/static/complementary.png",
        "base_colors": ["#674ea7"],
        "options": [
            {"color": "#ffd966", "is_correct": True},
            {"color": "#f6b26b", "is_correct": False},
            {"color": "#e06666", "is_correct": False},
            {"color": "#a4c2f4", "is_correct": False}
        ],
        "feedback_correct": "GREAT WORK",
        "feedback_incorrect": "NOT QUITE… TRY TO MAKE A COMPLEMENTARY OUTFIT AGAIN!",
        "next_question": "/quiz/4"
    },
    {
        "id": "4",
	"page_number": "4/4",
        "theme": "tetradic",
        "question_text": "PICK A PURSE COLOR TO MAKE A TETRADIC OUTFIT.",
        "image_url": "/static/tetradic.png",
        "base_colors": ["#cc0000", "#274e13", "#1c4587"],
        "options": [
            {"color": "#ffd966", "is_correct": True},
            {"color": "#f6b26b", "is_correct": False},
            {"color": "#674ea7", "is_correct": False},
            {"color": "#a4c2f4", "is_correct": False}
        ],
        "feedback_correct": "GREAT WORK",
        "feedback_incorrect": "NOT QUITE… TRY TO MAKE A TETRADIC OUTFIT AGAIN!",
        "next_question": "/results"
    }
]

#HOMEPAGE
@app.route('/')
def home_page():
   session.clear()
   return render_template('home.html')

#PAGE 1 and 2 of each combination (call dynamically)
@app.route('/learn/<number>a')
def lesson_one(number):
    # record page‐entry time
    session[f'lesson_{number}_entered_at'] = datetime.utcnow().isoformat()
    idx = int(number)-1
    lesson = learning_page1_data[idx]
    return render_template('lesson_one.html', lesson=lesson)

@app.route('/learn/<number>b')
def lesson_two(number):
    session[f'lesson_{number}_entered_at'] = datetime.utcnow().isoformat()
    idx = int(number)-1
    lesson = learning_page2_data[idx]
    return render_template('lesson_two.html', lesson=lesson)

# QUIZ ROUTE
@app.route('/quiz/<question_number>')
def quiz_question(question_number):
    try:
        if question_number == '1':
            session['score'] = 0
            session['answered_status'] = {}

        idx = int(question_number) - 1
        if 0 <= idx < len(quiz_data):
            question = quiz_data[idx]
            current_score = session.get('score', 0)
            return render_template('quiz.html', question=question, current_score=current_score)
        else:
            return render_template('home.html')
    except ValueError:
        return "Invalid question number", 400

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
	data = request.get_json()
	is_correct = data.get('is_correct')
	question_number = data.get('question_number')
	if is_correct:
		session['score'] = session.get('score', 0) + 1

	return jsonify({'score': session['score']})

# RESULTS PAGE
@app.route('/results')
def results_page():
    final_score = session.get('score', 0)
    total_questions = len(quiz_data)
    return render_template('results.html', score=final_score, total=total_questions)


if __name__ == '__main__':
   app.run(debug = True, port=5001)
