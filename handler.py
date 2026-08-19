import time
import requests

class NetworkError(Exception):
    pass

def retry_request(url, max_retries=3, backoff_factor=1):
    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.get(url)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()  # Return the response data as JSON
        except requests.exceptions.RequestException as e:
            attempts += 1
            if attempts == max_retries:
                raise NetworkError(f'Failed to connect after {max_retries} attempts')
            time.sleep(backoff_factor ** attempts)  # Exponential backoff

if __name__ == '__main__':
    url = 'https://api.example.com/data'
    try:
        data = retry_request(url)
        print(data)
    except NetworkError as e:
        print(e)