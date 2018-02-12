from bs4 import BeautifulSoup as bs
from urllib.request import urlopen
import csv

##url constructor
def get_url():
    BASE_URL = 'https://www.gismeteo.ru/diary/4079/'
    month_part = '/03/'
    year_part = ''
    urls = []
    for i in range(2000, 2018):
        year_part = str(i)
        url = BASE_URL + year_part + month_part
        urls.append(url)
    return urls

##parsing part 
##information from data tables on the each page
##which was constructed in the previous part
def finder(day):
    parsed_days = []
    for url in get_url():
        soup = bs(urlopen(url), 'html.parser')
        trs = soup.find_all('tr', align='center')
        weather = []

        for tr in trs:
            weather.append({
                'morning': (tr.find_all('td')[1].text),
                'evening': (tr.find_all('td')[6].text)
            })

        try:
           parsed_days.append(int(weather[day]['morning']))
        except IndexError:
            parsed_days.append(int(weather[day]['evening']))       

    return list(parsed_days)

##main part 
##making csv file 
def main():
    with open('march.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(range(2000, 2018))
        try:
            for day in range(32):
                writer.writerows([finder(day)])
                print('March', day+1)
        except IndexError:  
            print ('No more days')    
    print ('Done')    
    file.close()

if __name__ == '__main__':
    main()