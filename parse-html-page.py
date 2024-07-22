from bs4 import BeautifulSoup
import requests


def parse_html_page(url):
    """
    Parse an HTML page using BeautifulSoup.

    Parameters:
    - url (str): The URL of the HTML page to be parsed.

    Returns:
    BeautifulSoup object: Parsed HTML content.
    """
    try:
        # Make a GET request to the specified URL
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for bad responses

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        return soup

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


# Example usage
html_page_url = 'https://example.com'  # Replace with the actual URL of the HTML page
parsed_html = parse_html_page(html_page_url)

if parsed_html:
    # Now you can use 'parsed_html' to navigate and extract information from the HTML content
    # For example, extracting all the links in the HTML page:
    links = parsed_html.find_all('a')
    for link in links:
        print(link.get('href'))
