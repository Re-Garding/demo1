import googlemaps, os
from datetime import datetime
import requests

key = os.environ['MAPS']
gmaps = googlemaps.Client(key=f'{key}')

geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')

now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

dest = '8796 N Stonebridge Ln Eagle Mountain Utah 84005'
start = '14402 44th Ave SE North Bend WA 98045'
origin = gmaps.geocode(start)

params = {'destination': dest, 'origin' : f'place_id:{origin}'}

api_url = 'https://maps.googleapis.com/maps/api/directions/json'

keys = {'key' : key}
data = requests.get(api_url, params=params, Authorization=key )

print(data)