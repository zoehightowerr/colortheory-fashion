from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

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
      "color_amount": "3"
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
      "color_amount":"2"
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
      "color_amount":"3"
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
      "color_amount":"4"
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
      "outfit_1":"",
      "outfit_2":""
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
      "outfit_1":"",
      "outfit_2":""
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
      "outfit_1":"",
      "outfit_2":""
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
      "outfit_1":"",
      "outfit_2":""
   }
]

#HOMEPAGE
@app.route('/')
def home_page():
   return render_template('home.html') 

#PAGE 1 and 2 of each combonation (call dynamically)
@app.route('/learn/<number>a')
def lesson_one():
   #figure out data (theory, content, color_wheel, comment_text, popup_text, colors, color_amount)
   lesson= learning_page1_data[number]
   return render_template('lesson_one.html', lesson=lesson)
@app.route('/learn/<number>b')
def lesson_two():
   #figure out data (theory, content, bases, colors_1, colors_2, color_amount, outfit_1, outfit_2)
   lesson= learning_page2_data[number]
   return render_template('lesson_two.html', lesson=lesson)


if __name__ == '__main__':
   app.run(debug = True, port=5001)
