import httplib2

def get_places_type(query):
    http = httplib2.Http()

    place_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?'
    place_url += 'query=' + query
    place_url += '&key=AIzaSyB0bUsoDUBqfiCSLi-WizPzo7TivrGfZQ4'

    print(place_url)

    resp, content = http.request(place_url, method="GET", headers={'Content-type': 'application/json; charset=UTF-8'})

    print(content)
    return content

if __name__ == "__main__":
    print('Hello World')
    get_places_type('restaurants+in+Sydney')
