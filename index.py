import requests
from bs4 import BeautifulSoup

def get_page_title(url):
    
    try:
        # Send a request to the URL
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            # Parse the content of the page
            soup = BeautifulSoup(response.content, 'html.parser')

            # Extract the title of the page
            title = soup.title.string if soup.title else 'No Title Found'
            return title
        else:
            return "The request was not successful."
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == "__main__":
    title = get_page_title("https://www.pinterest.com")
    if len(title.split(' ')) > 1:
        print(title)
    else:
        print(f"The title of the page is: {title}")