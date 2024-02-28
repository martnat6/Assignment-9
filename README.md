# Assignment-9
Communication Contract

## Overview
- This microservice uses the Spotify Web API to provide recommendations based on user-provided genre input.
- To use the microservice, users need to obtain an API key and secret ID from the Spotify Developer API site: [Spotify Developer API](https://developer.spotify.com/documentation/web-api)

## Sending a Request
To request recommendations:
1. Send a GET request to the microservice endpoint.
2. Include the following parameters:
   - `Enter seed genres for recommendations (comma-separated):`: The user's preferred genre for recommendations.

Example Python call using `requests`:
```python
import requests

url = "http://your-microservice-url/api/data"
params = {"current_location": "your_current_location"}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    # Handle response data here
else:
    print("Failed to retrieve data from the microservice:", response.status_code)

## Receiving Data
The microservice will respond with recommendations in JSON format:

## Error Handling
- Handle non-200 status codes appropriately when receiving data from the microservice.
- Provide feedback or error messages to users in case of failed requests.
