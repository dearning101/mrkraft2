from flask import Flask, render_template, request
from scraper import scrape_horsepower, scrape_car_model

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/compare', methods=['POST'])
def compare():
    registration_number = request.form['registration_number']
    registration_number = registration_number.upper()

    # Anropa scrape_horsepower-funktionen för att hämta hästkraftsinformationen
    horsepower = scrape_horsepower(registration_number)

    # Anropa scrape_car_model-funktionen för att hämta bilmodellen
    car_model = scrape_car_model(registration_number)

    return render_template('result.html', registration_number=registration_number, horsepower=horsepower, car_model=car_model)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
