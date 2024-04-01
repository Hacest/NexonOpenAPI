import requests

def send_http_request(url):
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            print("HTTP request successful!")
            print("Response:")
            print(response.text)
        else:
            print("HTTP request failed with status code:", response.status_code)
    except requests.exceptions.RequestException as e:
        print("HTTP request failed:", e)

# Example usage:
url = "http://example.com"
send_http_request(url)