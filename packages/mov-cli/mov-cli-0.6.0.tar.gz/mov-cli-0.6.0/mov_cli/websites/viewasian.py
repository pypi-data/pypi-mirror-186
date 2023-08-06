from bs4 import BeautifulSoup as BS
from ..utils.scraper import WebScraper
import re

class viewasian(WebScraper):
    def __init__(self, base_url):
        super().__init__(base_url)
        self.base_url = base_url

    def search(self, q: str):
        q = (
            input(self.blue("[!] Please Enter the name of the Movie: "))
            if q is None
            else q
        )
        return q.replace(" ", "-")

    def results(self, data: str):
        request = self.client.get(f"{self.base_url}/movie/search/{data}")
        soup = BS(request, "lxml")
        streams = soup.findAll("a", {"class": "ml-mask jt"})
        urls = [streams[i]["href"] for i in range(len(streams))]
        title = [streams[i]["title"] for i in range(len(streams))]
        ids = [streams[i]["class"] for i in range(len(streams))]
        mov_or_tv = ["TV" for i in range(len(streams))]
        return [list(sublist) for sublist in zip(title, urls, ids, mov_or_tv)]

    def ask(self, url):
        request = self.client.get(f"{self.base_url}{url}")
        soup = BS(request, "lxml")
        href = soup.find("a", {"class":"bwac-btn"})["href"]
        request = self.client.get(f"{self.base_url}{href}")
        soup = BS(request, "lxml")
        episodes = soup.findAll("li", {"class": "ep-item"})
        episode = int(
                    input(
                        self.lmagenta(
                            f"Please input the episode number(Total: {len(episodes)}): "
                        )
                    )
                )
        request = self.client.get(f"{self.base_url}{href}?ep={episode}")
        soup = BS(request, "lxml")
        try:
            streamtape = soup.find("li", {"class": "streamtape"})["data-video"]
            dood = soup.find("li", {"class": "doodstream"})["data-video"]
            print("\r\nWhat Server do you want:\r\n[1] DoodStream\r\n[2] StreamTape")
            e = input("Please Enter what you want to use: ")
            if e == "1":
                li = self.doodstream(dood)
            elif e == "2":
                li = self.streamtape(streamtape)
            else:
                li = self.doodstream(dood)
        except:
            li = self.doodstream(soup.find("li", {"class": "doodstream"})["data-video"])
        return li, episode

    def streamtape(self, url):
        string = re.findall("""v\/([^"']*)\/""", url)[0]
        request = self.client.get(f"https://streamtape.com/e/{string}").text
        regex = r"""'robotlink'\)\.innerHTML = '(.*?)'\+ \('(.*?)'\)"""
        results = re.findall(regex, request)
        for tuple in results:
            url = tuple[0]
            rest = tuple[1]
        li = f"https:{url}{rest[3:]}"
        return li

    def doodstream(self, url):
        domain = re.findall("""([^"']*)\/e""", url)[0]
        req = self.client.get(url).text
        pass_md = re.findall(r"/pass_md5/[^']*", req)[0]
        token = pass_md.split("/")[-1]
        self.client.set_headers({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:108.0) Gecko/20100101 Firefox/108.0", "Referer": f"{url}", "Accept-Language": "en-GB,en;q=0.5"})
        drylink = self.client.get(f"{domain}{pass_md}").text
        streamlink = f"{drylink}zUEJeL3mUN?token={token}"
        print(streamlink)
        return streamlink

    def TV_PandDP(self, t: list, state: str = "d" or "p" or "sd"):
        name = t[self.title]
        url, episode = self.ask(t[self.url])
        if state == "d":
            self.dl(url, name, season=".", episode=episode)
            return
        self.play(url, name)



