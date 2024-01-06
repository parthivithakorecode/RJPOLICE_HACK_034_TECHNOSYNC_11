import time
import requests
from bs4 import BeautifulSoup
from rotating_proxies import RotatingProxies

def get_random_proxy():
        return "http://username:password@proxy.example.com:port"

def scrape_with_proxy(url, proxy):
    try:
        response = requests.get(url, proxies={'http': proxy, 'https': proxy})
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            # Process the webpage content as needed
            print(soup.title.text)
        else:
            print(f"Error accessing {url} with proxy. Status code: {response.status_code}")

    except Exception as e:
        print(f"Error while scraping with proxy: {str(e)}")

def time_based_proxy_scraping(url, proxy_list, interval_seconds):
    proxy_rotator = RotatingProxies(proxies=proxy_list)

    while True:
        try:
            proxy = get_random_proxy()
            print(f"Using proxy: {proxy}")
            
            # Use the proxy for scraping
            scrape_with_proxy(url, proxy)

            # Rotate to the next proxy after the specified interval
            time.sleep(interval_seconds)
            proxy_rotator.next_proxy()

        except KeyboardInterrupt:
            print("User interrupted the scraping.")
            break

if __name__ == "__main__":
    target_url = "https://example.com"
    
    
    proxy_list = ["http://proxy1.example.com", "http://proxy2.example.com", "http://proxy3.example.com"]
    
    
    interval_seconds = 60  # Change this based on your requirements

    time_based_proxy_scraping(target_url, proxy_list, interval_seconds)
