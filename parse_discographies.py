import json
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

def get_tree(soup: BeautifulSoup) -> ElementTree:
    with StringIO(soup.body.prettify()) as sp:
        return etree.parse(sp)

def get_transform(transform_path="bruckner.xslt") -> XSLT:
    with open(transform_path) as fp:
        xslt = etree.parse(fp)
        return etree.XSLT(xslt)

def transform_xml(xsl_template: XSLT, tree: etree) -> Any:
    return xsl_template(tree) 

def write_transformed_xml(filename, transformed_xml):
    with open(filename, mode="w") as fp:
        fp.write(transformed_xml)

def main():
    xsl_template=get_transform()

    export_spec = read_export_spec()
    export_dict = get_export_dict(export_spec)

    for url, destfile in export_dict.items():
        print(f"downloading {url}")
        tree = pipe(url,
                      download,
                      get_soup,
                      get_tree)
        result = transform_xml(xsl_template, tree)
        write_transformed_xml(destfile, str(result))

if __name__ == "__main__":
    main()
