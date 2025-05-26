# DoS Simulation Script - Run in Google Colab (educational use only)
import requests
from concurrent.futures import ThreadPoolExecutor
import time

# Target URL (should be your local Flask server endpoint)
target_url = "#copy the public ngrok URL of the Flask app"

# Function to send a request
def send_request():
    try:
        response = requests.get(target_url)
        print(f"Response: {response.status_code}")
    except Exception as e:
        print(f"Error: {e}")

# Simulate multiple rapid requests (potential DoS)
def simulate_dos(requests_per_second=100, duration=5):
    end_time = time.time() + duration
    with ThreadPoolExecutor(max_workers=50) as executor:
        while time.time() < end_time:
            for _ in range(requests_per_second):
                executor.submit(send_request)

simulate_dos()
