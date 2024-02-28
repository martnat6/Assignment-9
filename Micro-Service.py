import base64  # encode client id
import requests  # http requests


def get_access_token(client_id, client_secret):
    # Combine client ID and client secret with a colon, taken from spotify api website
    credentials = f"{client_id}:{client_secret}"

    # Encode the concatenated string with Base64
    encoded_credentials = base64.b64encode(credentials.encode()).decode()

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": f"Basic {encoded_credentials}"
    }
    data = {
        "grant_type": "client_credentials"
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Failed to obtain access token:", response.status_code)
        return None


def get_recommendations(location, access_token):
    url = "https://api.spotify.com/v1/recommendations"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    params = {
        "seed_genres": location
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        return data["tracks"]
    else:
        print("Failed to retrieve data from Spotify API:", response.status_code)
        return []


def main():
    client_id = "7e3b83c0e3214a429f243e8d0b444946"
    client_secret = "1de885876a684960bad977baa7a36646"
    location = input("Enter seed genres for recommendations (comma-separated): ")
    access_token = get_access_token(client_id, client_secret)
    if access_token:
        recommendations = get_recommendations(location, access_token)
        if recommendations:
            print("Received recommendations from Spotify API:")
            for recommendation in recommendations:
                print(f"{recommendation['name']} by {recommendation['artists'][0]['name']}")
        else:
            print("No recommendations received.")
    else:
        print("Exiting due to failure to obtain access token.")


if __name__ == "__main__":
    main()


