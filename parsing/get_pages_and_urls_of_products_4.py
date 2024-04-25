from bs4 import BeautifulSoup
from requests import Session, RequestException

def get_all_urls_of_products(url, session=None):
    if session is None:
        session = Session()

    products_url = []
    count = 1

    while True:
        full_url = f"{url}?page={count}"
        print(full_url)
        try:
            info = session.get(full_url)

            if not info.ok:
                print(f"Ошибка загрузки данных с {full_url}: {info.status_code}")
                break

            soup = BeautifulSoup(info.text, 'html.parser')
            links = soup.find_all('a', class_='linkToPDP active css-do8div')
            if not links:
                print("Нет дополнительных продуктов.")
                break

            for link in links:
                url_of_product = "https://www.auchan.ru" + link.get('href')
                products_url.append(url_of_product)

            count += 1

        except RequestException as e:
            print(f"Ошибка сети при попытке получить данные с {full_url}: {e}")
            break

    return products_url
