from flask import Flask, render_template, request, jsonify

# step 1: Create the flask app instance
app = Flask(__name__)

#step 2: # Dummy data for photographers
photographers = [
    {"id": "p1", "name": "Amit Lensman", "skills": ["Wedding", "Portrait"], "image": "amit.jpg"},
    {"id": "p2", "name": "Sana Clickz", "skills": ["Fashion", "Event"], "image": "sana.jpg"},
    {"id": "p3", "name": "Annie", "skills": ["Wedding", "Birthday"], "image": "annie.jpg"},
    {"id": "p4", "name": "Ansel", "skills": ["Wedding", "Private events"], "image": "ansel.jpg"},
    {"id": "p5", "name": "Cindy", "skills": ["Wedding", "Events"], "image": "cindy.jpg"},
]

availability_data = {
    "p1": ["2025-06-20","2025-06-23"],
    "p2": ["2025-06-19","2025-06-22"],
    "p3": ["2025-06-18","2025-06-21"],
    "p4": ["2025-06-17","2025-06-20"],
    "p5": ["2025-06-16","2025-06-19"]
}


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/')
def home():


     return render_template('home.html')


@app.route('/book', methods=['GET', 'POST'])
def book():

    if request.method == 'POST':
        photographer_id = request.form.get('photographer_id')
        date = request.form.get('date')
        return f"<h2 style='color:green'>Booking Confirmed! For {photographer_id} on {date}.</h2>"
    return render_template('book.html')


@app.route('/show-photographers')
def show_photographers():
    return render_template('photographers.html', photographers=photographers, availability_data=availability_data)

if __name__ == '__main__':
    app.run(debug=True)