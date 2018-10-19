# -*- coding: UTF-8 -*_
import urllib
import re


def getHtmlContent(url):
    page = urllib.urlopen(url)
    return page.read()


if __name__ == "__main__":
    url = 'http://tieba.baidu.com/p/2256306796'
    getHtmlContent(url)
