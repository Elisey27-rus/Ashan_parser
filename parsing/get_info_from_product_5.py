from bs4 import BeautifulSoup
from requests import Session

from get_curl_1 import get_info_from_culr  # Убедитесь, что эта функция также поддерживает сессии

session = Session()
def get_full_product_info(url, session=None):
    if session is None:
        from requests import Session
        session = Session()

    info = get_info_from_culr(url, session=session)

    if not info or not info.ok:
        print(f"Ошибка при загрузке страницы: {url}")
        return []

    soup = BeautifulSoup(info.text, 'html.parser')

    product_name_element = soup.find('h1', id='productName')
    product_name = product_name_element.text.strip() if product_name_element else "Название продукта не найдено"

    old_price_element = soup.find('div', class_='oldPricePDP')
    old_price = old_price_element.text.strip() if old_price_element else "0"
    old_price = ''.join(c for c in old_price if c.isdigit() or c == ',' or c == '.')

    new_price_element = soup.find('div', class_='fullPricePDP')
    new_price = new_price_element.text.strip() if new_price_element else "0"
    new_price = ''.join(c for c in new_price if c.isdigit() or c == ',' or c == '.')

    brand_element = soup.find('td', class_='css-em38yw')
    brand = brand_element.text.strip()
    print(product_name, old_price, new_price, brand)
    return [product_name, old_price, new_price, brand]
