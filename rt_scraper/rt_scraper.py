from bs4 import BeautifulSoup
from requests import get


def scrape(url):
    # Getting the html code
    source = get(url).text

    # Finding the list of the movies and parsing
    soup = BeautifulSoup(source, "lxml")
    div = soup.find("div", class_="panel-body content_body allow-overflow")
    table = div.find("table", class_="table")
    index = 1
    for tr in table.find_all("tr"):
        a = str(tr.find("a", class_="unstyled articleLink"))
        try:
            title = a.split(">")[1].split("</")[0].strip()
            print(f"{index}. {title}")
            index += 1
        except Exception: 
            pass
    print()


if __name__ == "__main__":

    urls = [
        "https://www.rottentomatoes.com/top/bestofrt/?year=2017",
        "https://www.rottentomatoes.com/top/bestofrt/?year=2018",
        "https://www.rottentomatoes.com/top/bestofrt/?year=2019"
    ]

    for url in urls:
        scrape(url)
