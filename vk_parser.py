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
import csv
from datetime import datetime


def export_to_csv(all_posts):
    file_name = input('Please enter name of file .csv\n')
    method = input('Choose:\n1 - Rewrite file\n2 - Append file\nOther to exit\n')
    if method == '1':
        mode = 'w'

    elif method == '2':
        mode = 'a'

    else:
        return

    with open(file_name, mode, encoding='utf-8') as csv_file:
        a_pen = csv.writer(csv_file)
        if mode == 'w':
            a_pen.writerow(('Date', 'Text', 'Likes', 'Comments', 'Views', 'Image URL'))
        for post in all_posts:
            try:
                if post['attachments'][0]['type']:
                    img_url = post['attachments'][0]['photo']['sizes'][-1]['url']
                else:
                    img_url = 'pass'
            except:
                img_url = 'pass'
            a_pen.writerow((datetime.utcfromtimestamp(post['date']).strftime('%Y-%m-%d %H:%M:%S'), post['text'],
                           post['likes']['count'], post['comments']['count'], post['views']['count'], img_url))

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
export_to_csv(all_posts)
