import json
import os
import requests

from collections.abc import Iterable, Mapping
from io import StringIO
from typing import Any

from bs4 import BeautifulSoup
from lxml import etree
from lxml.etree import ElementTree, XSLT
from toolz.functoolz import pipe

def read_export_spec(filename="export_spec.json") \
        -> Iterable[Mapping[str, str]]:
    with open(filename) as fp:
        return json.load(fp) 

def get_export_dict(export_spec:Iterable[Mapping[str, str]]) -> Mapping[str, str]:
    return {d["url"]:d["destfile"] for d in export_spec}

def download(url:str) -> str:
    rsp = requests.get(url)
    return rsp.text

def get_soup(html_text:str) -> BeautifulSoup:
    return BeautifulSoup(html_text, "html.parser")

def write_dest_file(soup: BeautifulSoup, destfile):
    with open("html_files/" + destfile[:-4] + ".html", mode="w") as fp:
        fp.write(soup.body.prettify())

def main():

    export_spec = read_export_spec()
    export_dict = get_export_dict(export_spec)
    for url, destfile in export_dict.items():
        soup  = pipe(url,
                     download,
                     get_soup)
        write_dest_file(soup, destfile) 
            


if __name__ == "__main__":
    main()
