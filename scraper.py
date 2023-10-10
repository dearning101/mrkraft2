import requests
from bs4 import BeautifulSoup

def scrape_horsepower(registration_number):
    try:
        # Skapa URL med det angivna registreringsnumret
        url = f'https://biluppgifter.se/fordon/{registration_number}'
        
        # Skicka en GET-förfrågan till den genererade URL:en
        response = requests.get(url)
        response.raise_for_status()  # Kasta ett fel om det uppstår något problem med förfrågan

        # Analysera HTML-svaret med BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        def is_valid_registration_number(registration_number):
            # Förväntad längd på registreringsnummer (exempelvis 6 tecken)
            expected_length = 6
            return len(registration_number) == expected_length

        # Iterera genom alla span-element med klassen "value"
        for span_element in soup.find_all('span', {'class': 'value'}):
            if "hk" in span_element.text:
                horsepower = span_element.text
                return horsepower

        # Om hästkraftsinformationen inte hittades, returnera ett felmeddelande
        return "Felaktigt registreringsnummer, vänligen försök igen"
    
    except requests.exceptions.HTTPError as http_err:
        return f"HTTP-fel: {http_err}"

    except Exception as err:
        return f"Fel vid webscraping: {err}"

# Ny funktion för att hämta bilmodellen
def scrape_car_model(registration_number):
    try:
        url = f'https://biluppgifter.se/fordon/{registration_number}'
        
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        # Sök efter bilmodellen baserat på HTML-strukturen på webbsidan
        model_element = soup.find('h1', {'class': 'card-title'})
        if model_element:
            car_model = model_element.text.strip()
            return car_model

        # Om bilmodellen inte hittades, returnera ett felmeddelande
        return "Bilmodell ej hittad"

    except requests.exceptions.HTTPError as http_err:
        return f"HTTP-fel: {http_err}"

    except Exception as err:
        return f"Fel vid webscraping: {err}"
