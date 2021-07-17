from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="mrizaln")
location = geolocator.geocode("Bandung")

address = location.address
latitude = location.latitude
longitude = location.longitude

# print(location.raw)

print(f'address: {address}\nlatitude: {latitude}\nlongitude: {longitude}')
