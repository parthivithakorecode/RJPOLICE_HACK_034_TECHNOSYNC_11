from bs4 import BeautifulSoup
import requests
from ipwhois import IPWhois

def analyze_webpage(ip_address):
    ip_details = get_ip_details(ip_address)
    print("IP Details:")
    print(ip_details)

def get_ip_details(ip_address):
    ipwhois = IPWhois(ip_address)
    result = ipwhois.lookup_rdap()

    # Extract relevant information from the result
    ip_details = {
        'ip': ip_address,
        'asn': result.get('asn'),
        'asn_cidr': result.get('asn_cidr'),
        'asn_country_code': result.get('asn_country_code'),
        'nets': result.get('nets'),
        'raw': result.get('raw'),
        'asn_description': result.get('asn_description'),
        'asn_registry': result.get('asn_registry'),
        'asn_date': result.get('asn_date'),
        'asn_cidr_raw': result.get('asn_cidr_raw'),
        'asn_cidr_network': result.get('asn_cidr_network'),
        'asn_cidr_range': result.get('asn_cidr_range'),
    }

    return ip_details

def extract_ip_from_webpage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract IP address from the page
            ip_address = get_ip_address_from_text(soup.text)
            return ip_address

    except Exception as e:
        print(f"Error extracting IP from webpage: {str(e)}")

    return None

def get_ip_address_from_text(text):
    
    import re
    ip_pattern = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')
    match = ip_pattern.search(text)
    return match.group() if match else None

# Example usage
if __name__ == "__main__":
    target_url = "https://example.com"
    
    # Extract IP address from the webpage
    ip_address = extract_ip_from_webpage(target_url)
    
    if ip_address:
        # Analyze the IP address
        analyze_webpage(ip_address)
    else:
        print("No IP address found on the webpage.")
