# ------------------------------------------------------
#
# Program by Eugene Koleda
#
#
#
# Version       Date        Info
# 1.0           2019    Initial Version
#
# ------------------------------------------------------

import requests


def take_posts():
    token = '61a1844761a1844761a18447e161c89f63661a161a184473ddee16e0614c997c0a312fe'
    version = 5.92
    all_posts = []
    domain_name = input('Please input link of a public\n').replace('https://vk.com/', '').replace(' ', '')
    if not domain_name:
        exit(0)
    amount = int(input('Enter amount of posts.\n'))
    offset = int(input('Enter offset for posts from the beginning.\n'))
    if amount > 100:
        count = amount % 100
    else:
        count = amount
    while count <= amount:
        response = requests.get('https://api.vk.com/method/wall.get',
                                params={
                                    'access_token': token,
                                    'v': version,
                                    'domain': domain_name,
                                    'count': count,
                                    'offset': offset
                                })
        data = response.json()['response']['items']
        all_posts.extend(data)
        offset += 100
        count += 100
    return all_posts


all_posts = take_posts()
