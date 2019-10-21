import httplib2


def get_places_type(query):
    http = httplib2.Http()

    place_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    place_url += 'query=' + query
    place_url += 'key=AIzaSyB0bUsoDUBqfiCSLi-WizPzo7TivrGfZQ4'

    resp, content = http.request(place_url, method="GET")

    return content
