import httplib2


def httpclient():
    http = httplib2.Http()


def get_placeinfo_Type(query):
    http = httplib2.Http()

    place_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
    place_url += 'query=' + query
    place_url += 'key=AIzaSyB0bUsoDUBqfiCSLi-WizPzo7TivrGfZQ4'

    resp, content = http.request(place_url, method="GET")
