import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool

def scrape_product(container):
    title_element = container.find('h2')
    title = title_element.text.strip()

    price_element = container.find('span', {'class': 'a-offscreen'})
    price = price_element.text.strip() if price_element else 'Not available'

    rating_element = container.find('span', {'class': 'a-icon-alt'})
    rating = rating_element.text.strip() if rating_element else 'Not rated'

    link_element = container.find('a', {'class': 'a-link-normal'})
    link = 'https://www.amazon.com' + link_element['href'] if link_element else 'Link not available'

    return {
        'title': title,
        'price': price,
        'rating': rating,
        'link': link
    }

def newsearch_amazon(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    product_containers = soup.find_all('div', {'data-component-type': 's-search-result'})

    with Pool() as pool:
        results = pool.map(scrape_product, product_containers)

    return results

results = newsearch_amazon("https://www.amazon.com/s?k=laptop")
print(results)