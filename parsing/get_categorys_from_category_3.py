from bs4 import BeautifulSoup
from get_curl_1 import get_info_from_culr
from requests import Session

session = Session()
def get_full_list_of_categories_of_category(url, session=None):
    if session is None:
        session = Session()

    info = get_info_from_culr(url, session=session)

    if info is None or not info.ok:
        print(f"Не удалось получить данные по URL: {url}")
        return []

    soup = BeautifulSoup(info.text, 'html.parser')

    links = soup.find_all('a', class_='linkToSubCategory active css-1bxu12v')
    result = []
    for link in links:
        href = "https://www.auchan.ru" + link.get('href')
        category_name = link.text.strip()
        result.append([href, category_name])

    return result


