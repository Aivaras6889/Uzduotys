from flask import Flask, render_template

app = Flask(__name__)
app.static_folder = 'templates/static'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/uzduotis_1')
def uzduotis_1():
    return render_template('uzduotis_1.html', greeting_A=pasisveikinimas, greeting_B="Sveiki Atvyke ... !!!")



"""Can be used with content from previous exercise:
Define a list of dictionaries containing information about multiple posts, including date, author, title, and content.
Pass this list to a template and iterate over each post to display its details.
Ensure proper formatting of dates and content in the template."""
skelbimai= [
{"id": 0, "author":"Antanas", "Title": "Atsiliepimas", "Content": "Tinkaimai suteiktos paslaugos ...."},
{"id": 1, "author":"Audrone", "Title": "Skelbimas", "Content": "Parduodu dvirati  uz 50eur."},
{"id": 3, "author":"Tomas", "Title": "Darbo Skelbimas", "Content": "Sveiki Ieskau darbo ... ."},
{"id": 4, "author":"Monika", "Title": "Korepetitoriaus paslaugos", "Content": "Sveiki siulau pagelbeti su papildomis matematikos paslaugomis ... ."},
]
@app.route('/uzduotis_2')
def uzduotis_2():

    return render_template('uzduotis_2.html', posts= skelbimai )

def pasisveikinimas(message):
    return message


if __name__ == '__main__': 
    app.run(debug=True)