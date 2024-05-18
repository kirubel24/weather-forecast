from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def get_current_weather(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        weather = {
            "description": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather
    else:
        return None

def get_next_day_forecast(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        # Assuming the next-day forecast is the first entry of the list
        next_day_forecast = data['list'][0]
        forecast = {
            "description": next_day_forecast['weather'][0]['description'],
            "temperature": next_day_forecast['main']['temp'],
            "humidity": next_day_forecast['main']['humidity'],
            "wind_speed": next_day_forecast['wind']['speed']
        }
        return forecast
    else:
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form.get("city")
        api_key = "c638652351cae2e1af93543dd3ac1ec5"  # Replace with your OpenWeatherMap API key
        current_weather = get_current_weather(api_key, city)
        next_day_forecast = get_next_day_forecast(api_key, city)
        if current_weather and next_day_forecast:
            return render_template("index.html", city=city, current_weather=current_weather, next_day_forecast=next_day_forecast)
        else:
            error_message = "Weather data not available."
            return render_template("index.html", error=error_message)
    else:
        return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
