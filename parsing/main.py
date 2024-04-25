import re

from requests import Session
from get_category_and_url_2 import get_category_and_url
from parsing.get_categorys_from_category_3 import get_full_list_of_categories_of_category
from parsing.get_info_from_product_5 import get_full_product_info
from parsing.get_pages_and_urls_of_products_4 import get_all_urls_of_products
import sqlite3

session = Session()
conn = sqlite3.connect("database.db")

try:
    categorys, categirys_urls = get_category_and_url(session=session)
    print(categorys)

    category = categorys[1]
    category_url = categirys_urls[1]
    category = re.sub(r'\s+', '_', category)
    category = re.sub(r'[()]+', '', category)
    print(category, "\n")
    print(category_url, "\n")
    final_list = []

    all_category_category = get_full_list_of_categories_of_category(category_url, session=session)
    print(all_category_category, "\n")

    for x in all_category_category:
        url = x[0]
        cursor = conn.cursor()
        cursor.execute(f"""
            CREATE TABLE IF NOT EXISTS {category} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                product_name TEXT NOT NULL,
                old_price TEXT,
                new_price TEXT,
                brand TEXT,
                url TEXT
            );
        """)
        result = get_all_urls_of_products(url, session=session)
        print(f'Категория {x[1]}')
        print(url)
        print(result)
        print(len(result))
        print('\n\n\n\n\n')

        for y in result:
            full_info = get_full_product_info(y, session=session)
            full_info.append(url)
            cursor.execute(f"""
                INSERT INTO {category} (product_name, old_price, new_price, brand, url)
                VALUES (?, ?, ?, ?, ?);
            """, (full_info[0], full_info[1], full_info[2], full_info[3], full_info[4]))

            conn.commit()

finally:
    conn.close()
    session.close()



