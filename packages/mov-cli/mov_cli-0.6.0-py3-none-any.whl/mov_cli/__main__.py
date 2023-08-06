import os
import sys
import platform

import click
from .utils.onstartup import startup

from .utils.scraper import WebScraper
from .websites.theflix import Theflix
from .websites.eja import eja
from .websites.ustvgo import ustvgo
from .websites.kimcartoon import kimcartoon
from .websites.actvid import Actvid
from .websites.dopebox import DopeBox
from .websites.sflix import Sflix
from .websites.solar import Solar
from .websites.viewasian import viewasian
from .websites.gogoanime import gogoanime
from .websites.watchasian import watchasian
from .websites.wlext import wlext
from .websites.streamblasters import streamblasters

calls = {
    "theflix": [Theflix, "https://theflix.to"],
    "eja" : [eja, "https://eja.tv"],
    "ustvgo": [ustvgo, "https://ustvgo.tv"],
    "kimcartoon": [kimcartoon, "https://kimcartoon.li"],
    "actvid": [Actvid, "https://www.actvid.com"],
    "sflix": [Sflix, "https://sflix.se"],
    "solar": [Solar, "https://solarmovie.pe"],
    "dopebox": [DopeBox, "https://dopebox.to"],
    "viewasian": [viewasian, "https://viewasian.co"],
    "gogoanime": [gogoanime, "https://www1.gogoanime.bid"],
    "watchasian": [watchasian, "https://watchasian.la"],
    "wlext": [wlext, "https://wlext.is"],
    "streamblasters": [streamblasters, "https://streamblasters.art"],
    }

try:
    startup.getkey()
except:
    print("You have exceeded Github's API Limit. You are not able to use the following Providers:\r\nActvid, SFlix, Dopebox, Solar\r\nTry using a Token\r\nSee: https://github.com/mov-cli/mov-cli/blob/v3/ghtoken.md")
    pass

if platform.system() == "Windows":
    os.system("color FF")  # Fixes colour in Windows 10 CMD terminal.

@click.command()
@click.option(
    "-p",
    "--provider",
    prompt=f"""\n
Movies and Shows:
theflix
actvid
sflix
solar
dopebox
wlext

Indian Movies and Shows:
streamblasters

Asian Movies and Shows:
viewasian
watchasian

Anime:
gogoanime

Live TV:
eja
ustvgo / US IP ONLY
    
Cartoons:
kimcartoon
    
The name of the provider""",
    help='The name of the provider ex: "theflix"',
    default=f"actvid",
)
@click.option("-q", "--query", default=None, help="Your search query")
@click.option(
    "-r",
    "--result",
    default=None,
    help="The Result Number you want to be played",
    type=int,
)
def movcli(provider, query, result):  # TODO add regex
    try:
        provider_data = calls.get(provider, calls["actvid"])
        provider:WebScraper = provider_data[0](provider_data[1])
            # provider.redo(query) if query is not None else provider.redo()
        provider.redo(query, result)  # if result else provider.redo(query)
    except UnicodeDecodeError:
        print("The Current Provider has changed")
    except Exception as e:
        print("[!] An error has occurred | ", e)

if __name__ == '__main__':
    movcli()
