Weather Forecast Application

This Weather Forecast Application is a simple web application built using Flask, a lightweight web framework for Python. The application fetches current weather data and next day weather forecast for a specified city using the OpenWeatherMap API and displays it on a web page.

Features

-Fetch current weather data for a specified city.
-Fetch next day weather forecast for the specified city.
-Display weather information including description, temperature, humidity, and wind speed.
-Error handling for cases where weather data is not available.

Technologies Used

-Python
-Flask
-HTML
-CSS
-Jinja2 Templating
-OpenWeatherMap API

To run the Weather Forecast Python script, follow these steps:

1. Get your own API key from [OpenWeatherMap](https://openweathermap.org/) by creating an account. Put the API key into the `weather.py` script on line 25 where it says `"YOUR_API_KEY"`. (Note: We've included our own API key in the script, so you only need to replace it if it's not working.)

2. Make sure you have Python installed on your system. If not, download it from the [official Python website](https://www.python.org/).

3. Install Flask if you haven't already by running `pip install flask` in your terminal or command prompt.

4. Open the command prompt or terminal on your computer.

5. Navigate to the directory where your `weather.py` file is located using the `cd` command followed by the path to the directory. For example: `cd path/to/the/project`.

6. Once you're in the correct directory, run the Python script using the `python` command. For example: `python weather.py`.

7. Once the Flask application is running, it will display a local URL (usually `http://127.0.0.1:5000/`). Open this URL in your web browser.

8. Enter the desired city to forecast the weather, then click the "Get Forecast" button.
