from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'c24t8uncg48tyn0c4t0q4375q2350v4' # I smash my keyboard generating this. to generate your API key, go to darksky.net

darksky = DarkSky(API_KEY)

latitude = -6.9344694
longitude = 107.6049539
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

# summ = f'summary    : {forecast.currently.summary}'
# temp = f'temperature: {forecast.currently.temperature} \N{DEGREE SIGN}C'
# humi = f'humidity   : {forecast.currently.humidity} %'
# pres = f'pressure   : {forecast.currently.pressure/10} kPa'

# weather = {
#     'summary': summ,
#     'temperature': temp,
#     'humidity': humi,
#     'pressure': pres
#     }

weather = forecast.currently.summary

from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    title = "Homepage"
    return render_template("index.html", title = title, weather = weather)

@app.route("/about")
def about():
    title = "About"
    return render_template("about.html", title = title, weather = weather)

@app.route("/contact")
def contact():
    title = "Contact"
    return render_template("contact.html", title = title, weather = weather)
