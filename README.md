# Assignment-9
Communication Contract
- I am using the spotify web API to recieve reccomendations based on given user genre input. This will not change.

 To send a request:
- Send a GET requst to the endpoint of spotify api.
- Example call:

import requests

url = "http://microservice-url/api/data"
params = {"current_location": "your_current_location"}

response = requests.get(url, params=params)


Receiving Data:

HTTP Response: The microservice will send back an HTTP response in JSON format.
Example Response:
json
{
  "recommendations": [
    {
      "song_title": "Example Song 1",
      "artist": "Artist 1"
    },
    {
      "song_title": "Example Song 2",
      "artist": "Artist 2"
    },
    ...
  ]
}
