# Заходим  на страницу которую будем парсить, заходим в детали кода, во вкладке network копируем нажимаем на самый первый name и кипируем его URL

# переходим на этот вебсайт    website="https://curlconverter.com/" и туда вводим:

# URL="curl 'https://www.auchan.ru/?from=supertseny_1' \
#   -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
#   -H 'Accept-Language: en,ru;q=0.9' \
#   -H 'Cache-Control: max-age=0' \
#   -H 'Connection: keep-alive' \
#   -H 'Cookie: haveChat=true; mindboxDeviceUUID=2c26b5c0-dfbb-4e09-b196-06794b670771; directCrm-session=%7B%22deviceGuid%22%3A%222c26b5c0-dfbb-4e09-b196-06794b670771%22%7D; tmr_lvid=c20ea4f1e4da17d0727901f51075d417; tmr_lvidTS=1713855432470; region_id=1; merchant_ID_=1; methodDelivery_=1; _GASHOP=001_Mitishchi; _ym_uid=1713855433145637451; _ym_d=1713855433; _ym_isad=2; _userGUID=0:lvc19vg6:IUjQFQYBVW5FsHsVbTbT3aXBsOcHzz~c; rrpvid=234514432567492; rcuid=660bc2789028635cd50618fa; _ymab_param=UhZCa087DA6FbaSbNMyxTTWqa2z03pb1rnG-HMDtzwP2q7-AQ35IIvzr-pq798ORRuZb1Hww1Ct229U3f-QIDObhvss; motopopupforeveryone=1; _clck=1osh4h9%7C2%7Cfl6%7C0%7C1574; digi_uc=W10=; acceptCookies_=true; _ym_visorc=w; _clsk=zg7ty4%7C1713879979688%7C2%7C1%7Cr.clarity.ms%2Fcollect; qrator_jsid=1713879376.492.bmhyPlg1LUv9EOz3-f7c4k7q2c146rhf7fuljm6oopp4je4fl; dSesn=b20f693a-e126-f79f-451f-8a344c7192e5; _dvs=0:lvcfwn0h:qZ8AdbYEv4iGAwG4uyu7JcLZR142BgzA; tmr_detect=0%7C1713880047800' \
#   -H 'Referer: https://www.auchan.ru/' \
#   -H 'Sec-Fetch-Dest: document' \
#   -H 'Sec-Fetch-Mode: navigate' \
#   -H 'Sec-Fetch-Site: same-origin' \
#   -H 'Sec-Fetch-User: ?1' \
#   -H 'Upgrade-Insecure-Requests: 1' \
#   -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36' \
#   -H 'sec-ch-ua: "Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"' \
#   -H 'sec-ch-ua-mobile: ?0' \
#   -H 'sec-ch-ua-platform: "macOS"'"

# Выдаст ответ----->


import requests
from requests import Session
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


session = Session()


def get_info_from_culr(url, session=None):
    if session is None:
        session = Session()

    cookies = {
        'haveChat': 'true',
        'mindboxDeviceUUID': '2c26b5c0-dfbb-4e09-b196-06794b670771',
        'directCrm-session': '%7B%22deviceGuid%22%3A%222c26b5c0-dfbb-4e09-b196-06794b670771%22%7D',
        'tmr_lvid': 'c20ea4f1e4da17d0727901f51075d417',
        'tmr_lvidTS': '1713855432470',
        'methodDelivery_': '1',
        '_ym_uid': '1713855433145637451',
        '_ym_d': '1713855433',
        '_userGUID': '0:lvc19vg6:IUjQFQYBVW5FsHsVbTbT3aXBsOcHzz~c',
        'rrpvid': '234514432567492',
        'rcuid': '660bc2789028635cd50618fa',
        '_ymab_param': 'UhZCa087DA6FbaSbNMyxTTWqa2z03pb1rnG-HMDtzwP2q7-AQ35IIvzr-pq798ORRuZb1Hww1Ct229U3f-QIDObhvss',
        'motopopupforeveryone': '1',
        'acceptCookies_': 'true',
        '_clck': '1osh4h9%7C2%7Cfl8%7C0%7C1574',
        '_ym_isad': '2',
        'device_id': '984624594319.4731',
        'rrlevt': '1714043023862',
        'digi_uc': 'W1sidiIsIjkyMTUxNSIsMTcxNDA0MzAyNDA2NV0sWyJ2IiwiMTE1OTA5IiwxNzE0MDQwMjczNjMzXSxbInYiLCJ1bmRlZmluZWQiLDE3MTQwMzc3NjkyNzJdLFsidiIsIjEyNTk1MSIsMTcxMzk3NDM0NzkwOF0sWyJ2IiwiNzM5NDgyIiwxNzEzOTc0MDQyMTY0XSxbInYiLCI3ODMwODgiLDE3MTM5NzMyNTU0MDRdLFsidiIsIjgyNDQ1MSIsMTcxMzg5OTM1MzExN10sWyJ2IiwiMzU2MjM5IiwxNzEzODk2NjM3ODU3XV0=',
        'isLoyaltyActivationPopupShown_': 'true',
        'isLoyaltyUser_': 'true',
        'access_token_': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzZWI2NDI0Mi1hMzgwLTRlNzEtYTZlMC1kZTgyMzJlMGM4NjkiLCJpYXQiOjE3MTQwNDM3NTAsInN1YiI6IjczYTY5Nzc0LTUwOTMtNDlkZS1iODI5LWUxZjkwMTY3OWIzOCIsImxldmVsIjo4MCwiaXNzIjoiQXVjaGFuLnJ1IiwiZXhwIjoxNzIxODE5NzUwfQ.cb0xPaDAU8VdvZ9LfXVc8lxc6OMkl2VKqkEunslh6Wk',
        '_GAUSERID': '24374831',
        'isPersonalGreetingPopupShown_': 'true',
        '_dvs': '0:lvfbg2zv:FMFEFHUyrFAuZFFwCsijWr1x54FToHE9',
        '_ym_visorc': 'w',
        '_clsk': 'fq7aqw%7C1714064574226%7C22%7C1%7Cr.clarity.ms%2Fcollect',
        'tmr_detect': '0%7C1714065019362',
        'address_': '%7B%22address_string%22%3A%22%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%2C%20%D1%83%D0%BB%20%D0%94%D1%8B%D0%B1%D0%B5%D0%BD%D0%BA%D0%BE%2C%20%D0%B4%205%20%D0%BA%206%22%2C%22area%22%3Anull%2C%22city%22%3A%22%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%2C%22block%22%3A%22%D0%BA%206%22%2C%22house%22%3A%22%D0%B4%205%22%2C%22region%22%3A%22%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%2C%22street%22%3A%22%D1%83%D0%BB%20%D0%94%D1%8B%D0%B1%D0%B5%D0%BD%D0%BA%D0%BE%22%2C%22geo_lat%22%3A%2259.898124%22%2C%22geo_lon%22%3A%2230.454649%22%2C%22post_index%22%3A%22193230%22%2C%22country_code%22%3A%22RU%22%2C%22area_guid%22%3Anull%2C%22city_guid%22%3A%22c2deb16a-0330-4f05-821f-1d09c93331e6%22%2C%22region_guid%22%3A%22c2deb16a-0330-4f05-821f-1d09c93331e6%22%2C%22settlement_with_type%22%3A%22%22%7D',
        '_GASHOP': '101_Dibenko',
        'merchant_ID_': '101',
        'region_id': '2',
        'qrator_jsid': '1714063752.570.TS4xWz2DXBV9XFpi-mah4iuom69emrn1mua90pp9pqnsrj1uv',
    }

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'Accept-Language': 'en,ru;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        # 'Cookie': 'haveChat=true; mindboxDeviceUUID=2c26b5c0-dfbb-4e09-b196-06794b670771; directCrm-session=%7B%22deviceGuid%22%3A%222c26b5c0-dfbb-4e09-b196-06794b670771%22%7D; tmr_lvid=c20ea4f1e4da17d0727901f51075d417; tmr_lvidTS=1713855432470; methodDelivery_=1; _ym_uid=1713855433145637451; _ym_d=1713855433; _userGUID=0:lvc19vg6:IUjQFQYBVW5FsHsVbTbT3aXBsOcHzz~c; rrpvid=234514432567492; rcuid=660bc2789028635cd50618fa; _ymab_param=UhZCa087DA6FbaSbNMyxTTWqa2z03pb1rnG-HMDtzwP2q7-AQ35IIvzr-pq798ORRuZb1Hww1Ct229U3f-QIDObhvss; motopopupforeveryone=1; acceptCookies_=true; _clck=1osh4h9%7C2%7Cfl8%7C0%7C1574; _ym_isad=2; device_id=984624594319.4731; rrlevt=1714043023862; digi_uc=W1sidiIsIjkyMTUxNSIsMTcxNDA0MzAyNDA2NV0sWyJ2IiwiMTE1OTA5IiwxNzE0MDQwMjczNjMzXSxbInYiLCJ1bmRlZmluZWQiLDE3MTQwMzc3NjkyNzJdLFsidiIsIjEyNTk1MSIsMTcxMzk3NDM0NzkwOF0sWyJ2IiwiNzM5NDgyIiwxNzEzOTc0MDQyMTY0XSxbInYiLCI3ODMwODgiLDE3MTM5NzMyNTU0MDRdLFsidiIsIjgyNDQ1MSIsMTcxMzg5OTM1MzExN10sWyJ2IiwiMzU2MjM5IiwxNzEzODk2NjM3ODU3XV0=; isLoyaltyActivationPopupShown_=true; isLoyaltyUser_=true; access_token_=eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIzZWI2NDI0Mi1hMzgwLTRlNzEtYTZlMC1kZTgyMzJlMGM4NjkiLCJpYXQiOjE3MTQwNDM3NTAsInN1YiI6IjczYTY5Nzc0LTUwOTMtNDlkZS1iODI5LWUxZjkwMTY3OWIzOCIsImxldmVsIjo4MCwiaXNzIjoiQXVjaGFuLnJ1IiwiZXhwIjoxNzIxODE5NzUwfQ.cb0xPaDAU8VdvZ9LfXVc8lxc6OMkl2VKqkEunslh6Wk; _GAUSERID=24374831; isPersonalGreetingPopupShown_=true; _dvs=0:lvfbg2zv:FMFEFHUyrFAuZFFwCsijWr1x54FToHE9; _ym_visorc=w; _clsk=fq7aqw%7C1714064574226%7C22%7C1%7Cr.clarity.ms%2Fcollect; tmr_detect=0%7C1714065019362; address_=%7B%22address_string%22%3A%22%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%2C%20%D1%83%D0%BB%20%D0%94%D1%8B%D0%B1%D0%B5%D0%BD%D0%BA%D0%BE%2C%20%D0%B4%205%20%D0%BA%206%22%2C%22area%22%3Anull%2C%22city%22%3A%22%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%2C%22block%22%3A%22%D0%BA%206%22%2C%22house%22%3A%22%D0%B4%205%22%2C%22region%22%3A%22%D0%B3%20%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%22%2C%22street%22%3A%22%D1%83%D0%BB%20%D0%94%D1%8B%D0%B1%D0%B5%D0%BD%D0%BA%D0%BE%22%2C%22geo_lat%22%3A%2259.898124%22%2C%22geo_lon%22%3A%2230.454649%22%2C%22post_index%22%3A%22193230%22%2C%22country_code%22%3A%22RU%22%2C%22area_guid%22%3Anull%2C%22city_guid%22%3A%22c2deb16a-0330-4f05-821f-1d09c93331e6%22%2C%22region_guid%22%3A%22c2deb16a-0330-4f05-821f-1d09c93331e6%22%2C%22settlement_with_type%22%3A%22%22%7D; _GASHOP=101_Dibenko; merchant_ID_=101; region_id=2; qrator_jsid=1714063752.570.TS4xWz2DXBV9XFpi-mah4iuom69emrn1mua90pp9pqnsrj1uv',
        'Referer': 'https://www.google.com/',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'cross-site',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }



    try:
        response = session.get(url, headers=headers, cookies=cookies, timeout=10)
        return response
    except requests.RequestException as e:
        print(f"Error during request: {e}")
        return None