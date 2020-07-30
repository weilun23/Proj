import bs4 as bs
import sys
import urllib.request
from PyQt5.QtWebEngineWidgets import QWebEnginePage
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QUrl

import pycurl
import certifi
import io
import json


class Page(QWebEnginePage):
    def __init__(self, url):
        self.app = QApplication(sys.argv)
        QWebEnginePage.__init__(self)
        self.html = Page.auth(url)
        self.loadFinished.connect(self._on_load_finished)
        self.load(QUrl(url))
        self.app.exec_()

    def _on_load_finished(self):
        self.html = self.toHtml(self.Callable)
        print('Load finished')

    def Callable(self, html_str):
        self.html = html_str
        self.app.quit()

    @staticmethod
    def auth(url):
        e = io.BytesIO()
        c = pycurl.Curl()
        c.setopt(c.URL, url)
        c.setopt(pycurl.WRITEFUNCTION, e.write)
        c.setopt(pycurl.FOLLOWLOCATION, 1)
        c.setopt(c.CAINFO, certifi.where())
        c.setopt(c.VERBOSE, True)
        c.perform()
        print('Status: %d' % c.getinfo(c.RESPONSE_CODE))
        c.close()
        strhtml = e.getvalue().decode('utf-8')
        return strhtml


def main():
    page = Page('https://www.youtube.com/')
    soup = bs.BeautifulSoup(page.html, 'html.parser')
    js_test = soup.find('div', attrs={'class': 'm9osqain a5q79mjw'})
    print(js_test)


main()
