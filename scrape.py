# Import necessary modules from your package
from my_scraper.request_handler import make_api_request
from my_scraper.data_parser import parse_api_response
from my_scraper.export_data import export_to_csv

if __name__ == "__main__":
    # Define the API endpoint URL 
    api_url = "https://www.earthdata.nasa.gov/engage/open-data-services-and-software/api"

    # Make an HTTP GET request to the API endpoint
    response = make_api_request(api_url)

    if response is not None:
        # Parse the JSON response
        data = parse_api_response(response)

        if data is not None:
            # Convert the data to a DataFrame (replace with actual parsing logic)
            df = pd.DataFrame(data)

            # Export the data to a CSV file
            export_to_csv(df, "time_series_data.csv")
            print("Data exported to time_series_data.csv")
        else:
            print("Error: Unable to parse API response.")
    else:
        print("Error: Unable to fetch data from the API.")

import requests

def make_api_request(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()  # Raise an exception for 4xx or 5xx status codes
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {str(e)}")
        return None

def parse_api_response(response):
    try:
        data = response.json()
        return data
    except ValueError:
        print("Error: Unable to parse JSON response.")
        return None

def export_to_csv(df, filename):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        print(f"Error: {str(e)}")
