import requests
from bs4 import BeautifulSoup
import csv
import time

def blog_crawling(page=1):
    url = "https://search.naver.com/search.naver?" \
          "where=post&sm=tab_jum&query=%EC%95%A0%EA%B2%AC+%EC%82%B0%EC%B1%85".format(page)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')

    blog_post_list = []

    for links in soup.select('li.sh_blog_top > dl'):
        title = links.select('dt > a')
        content = links.select('dd.sh_blog_passage')
        author = links.select('dd.txt_block a')

        title = title[0].get('title')
        content = content[0].text
        author = author[0].text

        blog_post = {'author':author, 'title':title, 'content':content}
        print(blog_post)

        blog_post_list.append(blog_post)

    return blog_post_list


def save_data(blog_post):
    keys = blog_post[0].keys()
    with open('blog_crawling.csv','w') as file:
        writer = csv.DictWriter(file, keys)
        writer.writeheader()
        writer.writerows(blog_post)

blog_post_list = []
for i in range(1, 100, 10):
    blog_post_list.extend(blog_crawling(page=i))
    time.sleep(2)

save_data(blog_post_list)




