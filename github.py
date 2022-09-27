import requests
from bs4 import BeautifulSoup as bs
from csv import writer
import pandas as pd

class GithubDataScraper:

    def get_github_data(self, url):

        page = requests.get(url)
        # print(page)
        soup = bs(page.content, 'html.parser')
        lists = soup.find_all('li', class_="col-12")

        with open('github.csv', 'w', encoding='utf8', newline='') as f:

            thewriter = writer(f)
            header = ['Name', 'Type', 'Technology', 'Stars']
            thewriter.writerow(header)

            for list in lists:

                Name = list.find('div', class_="col-10"). \
                    find('h3', class_="wb-break-all").find('a').text.strip()

                Type = list.find('div', class_="col-10"). \
                    find('h3', class_="wb-break-all"). \
                        find('span', class_="Label").text.strip()

                Technology = list.find('div', class_="col-10").\
                    find('div', class_="f6").find('span', class_="ml-0")

                Stars = list.find('div', class_="col-10").\
                    find('div', class_="f6").find('a', class_="Link--muted")
                
                info = [Name, Type, Technology, Stars]
                thewriter.writerow(info)


if __name__ == "__main__":

    obj_github_data_scraper = GithubDataScraper()

    obj_github_data_scraper.get_github_data('https://github.com/buckyroberts?tab=repositories')