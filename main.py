from bs4 import BeautifulSoup
import requests

dictinary = dict()
post_number = 1

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:50.0) Gecko/20100101Firefox/50.0'}
html_text = requests.get('https://divar.ir/s/tehran/vehicles').text
soup = BeautifulSoup(html_text, 'lxml')
main_tags = soup.find_all('div', class_='post-card-item-af972 kt-col-6-bee95 kt-col-xxl-4-e9d46')

for tag in main_tags:

    car_post_name = tag.find('h2', class_='kt-post-card__title').text
    car_price_kilometer = tag.find_all('div', class_='kt-post-card__description')

    car_post_time = tag.find('span', class_='kt-post-card__bottom-description kt-text-truncate')

    if bool(car_post_time) == False:
        car_post_time = tag.find('span', class_='kt-post-card__red-text')

    if len(car_price_kilometer) == 2:
        kilo = car_price_kilometer[0]
        price = car_price_kilometer[1]
        print(f"""
         POST {str(post_number)}-----------

            Name : {car_post_name} ,
            Car kilometer : {kilo.text}
            Car price : {price.text}
            Post time : {car_post_time.text}
            
            """)
        dictinary[post_number] = {}
        dictinary[post_number]["Car Name"] = car_post_name
        dictinary[post_number]["Cars Kilometer"] = kilo.text
        dictinary[post_number]["Car Price"] = price.text
        dictinary[post_number]["Time of post"] = car_post_time.text

        post_number += 1


    else:

        car_price_kilometer = 'توافقی'

        print(f"""
         POST {str(post_number)}-----------

        Name : {car_post_name} ,
        Car kilometer : -
        Car price : {car_price_kilometer}
        Post time : {car_post_time.text}

        """)
        dictinary[post_number] = {}
        dictinary[post_number]["Car Name"] = car_post_name
        dictinary[post_number]["Cars Kilometer"] = car_price_kilometer
        dictinary[post_number]["Car Price"] = car_price_kilometer
        dictinary[post_number]["Time of post"] = car_post_time.text

        post_number += 1

#pprint.pprint(dictinary)






