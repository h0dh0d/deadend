# fetch_data.py
import requests
import json

def main():
    url = "https://gatsby.bl3ebird.workers.dev"
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP errors
    data = response.json()

    # Save the data to a JSON file
    with open('data.json', 'w') as f:
        json.dump(data, f, indent=4)

if __name__ == "__main__":
    main()
