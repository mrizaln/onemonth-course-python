from darksky.api import DarkSky
from darksky.types import languages, units, weather


API_KEY = 'e2fea81b36c2588f1315c4ad2b721989'

darksky = DarkSky(API_KEY)

latitude = -7.324664
longitude = 108.339546
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print(f'summary    : {forecast.currently.summary}')
print(f'temperature: {forecast.currently.temperature}  \N{DEGREE SIGN}C')
print(f'humidity   : {forecast.currently.humidity}   %')
print(f'pressure   : {forecast.currently.pressure/10} kPa')

forecast.latitude # 42.3601
forecast.longitude # -71.0589
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. Can be finded at darksky/forecast.py
forecast.minutely # MinutelyForecast. Can be finded at darksky/forecast.py
forecast.hourly # HourlyForecast. Can be finded at darksky/forecast.py
forecast.daily # DailyForecast. Can be finded at darksky/forecast.py
forecast.alerts # [Alert]. Can be finded at darksky/forecast.py