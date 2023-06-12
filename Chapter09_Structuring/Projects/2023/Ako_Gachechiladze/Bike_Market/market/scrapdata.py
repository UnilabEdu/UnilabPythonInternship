from bs4 import BeautifulSoup
import requests

USD = 2.58

names = []
about = []
prices = []
images = []

URLS = ['https://www.competitivecyclist.com/custom-mountain-bikes-frames']


def scrap_parts(parts_url):
    page = 1
    url = f'{parts_url}'
    src = requests.get(url).text
    soup = BeautifulSoup(src, 'lxml')
    # images
    fork_image = soup.find_all('img', class_="chakra-image css-a8mvan")
    for image in fork_image:
        endpoint = str(image).split('"')[13]
        images.append(f"https:{endpoint}")

    # names
    fork_name = soup.find_all('p', class_="chakra-text css-nxn9mj")
    fork_about = soup.find_all('h2', class_="chakra-heading css-1gfqank")
    for i, name in enumerate(fork_name):
        names.append(name.text)
        about.append(fork_about[i].text)

    # price
    fork_price = soup.find_all('span', class_="chakra-text css-17wknbl")
    for price in fork_price:
        usd_to_gel = int(price.text.split("$")[1].replace(",", "").split(".")[0]) * USD
        prices.append(round(usd_to_gel, 2))

    page += 1

    part_name = 'frame'
    return part_name


def scrapped_data():
    data = []
    for url in URLS:
        part_name = scrap_parts(url)
        for j in range(len(names)):
            try:
                item = {
                    'name': names[j],
                    'about': about[j],
                    'price': prices[j],
                    'image': images[j],
                    'part_name': part_name
                }
                data.append(item)
            except:
                pass
    return data

