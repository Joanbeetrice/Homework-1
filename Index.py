import pandas as pd
import requests

# API endpoint URL
api_url = "https://data.cityofnewyork.us/resource/5fn4-dr26.json"

# Send a GET request to the API endpoint
response = requests.get(api_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Convert the JSON response to a DataFrame
    data = response.json()
    df = pd.DataFrame(data)

    # Display the DataFrame
    print(df.head())
else:
    # Print an error message if the request was not successful
    print(f"Error: {response.status_code}")

