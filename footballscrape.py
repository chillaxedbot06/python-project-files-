

import requests
from bs4 import BeautifulSoup


def job():
        src = requests.get('https://www.washingtonfootball.com/').text
        soup = BeautifulSoup(src, 'lxml')

        fh = open(r'C:\Users\Vishu\OneDrive - Prince William County Public Schools\Desktop\impy\footballinfo.txt', 'w')
        fh.close()
        fhand = open(r'C:\Users\Vishu\OneDrive - Prince William County Public Schools\Desktop\impy\footballinfo.txt', 'w')

        all_big = soup.find_all('ol', class_='nfl-o-headlinestack__list')
        headline_big = all_big[0]
        video_big = all_big[1]
        podcast_big = all_big[2]
        url = "https://washingtonfootball.com"
        fhand.write('Headlines')
        fhand.write("\n")


        for li in headline_big.find_all('li'):
            story = li.div.a['data-link_name']
            indurl = li.div.a['href']
            print(story, url + indurl)
            print('\n')
            fhand.write(story + " " + url + indurl)
            fhand.write('\n')
        fhand.write('--------------------------')


        fhand.write('\n')
        fhand.write('Videos')
        fhand.write('\n')


        for li in video_big.find_all('li'):
            story = li.div.a['data-link_name']
            indurl = li.div.a['href']
            print(story, url + indurl)
            print('\n')
            fhand.write(story + " " + url + indurl)
            fhand.write('\n')
        fhand.write('--------------------------')


        fhand.write('\n')
        fhand.write('Podcasts')
        fhand.write('\n')


        for li in podcast_big.find_all('li'):
            story = li.div.a['data-link_name']
            indurl = li.div.a['href']
            print(story, url + indurl)
            print('\n')
            fhand.write(story + " " + url + indurl)
            fhand.write('\n')
        
            fhand.close()
job()
