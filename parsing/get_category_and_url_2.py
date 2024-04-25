from bs4 import BeautifulSoup
from requests import Session
from get_curl_1 import get_info_from_culr

session = Session()
def get_category_and_url(session=None):
    if session is None:
        session = Session()

    url = "https://www.auchan.ru/"
    response = get_info_from_culr(url, session=session)

    if response is None:
        print("Ошибка получения данных с сайта.")
        return [], []

    soup = BeautifulSoup(response.text, "html.parser")

    links = soup.find_all("a", class_='youMayNeedCategoryItem active css-1poaokp')

    all_categories = []
    categories_urls = []

    for link in links:
        category_name = link.get_text(strip=True)
        category_url = "https://www.auchan.ru" + link.get('href')
        all_categories.append(category_name)
        categories_urls.append(category_url)

    return all_categories, categories_urls


