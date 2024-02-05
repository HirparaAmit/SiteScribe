import requests
from bs4 import BeautifulSoup

def scrape_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the response

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract text content
        text_content = soup.get_text()

        # Save the text content to a file
        with open('output.txt', 'w', encoding='utf-8') as file:
            file.write(text_content)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

# Replace 'your_website_url' with the actual URL you want to scrape
website_url = 'https://www.apple.com/in/macbook-pro/'
scrape_website(website_url)
