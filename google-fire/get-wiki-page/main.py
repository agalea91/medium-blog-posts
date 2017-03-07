#!/usr/bin/env python
'''
A class for getting wiki-page data.
For usage instructions execute the following lines:
>>> python main.py -- --help
>>> python main.py get-html-element -- --help
'''
import fire
import requests
import re

class WikiPage():
    '''
    Request a wikipedia page.
    
    page : str
        The page URL. Will return a random page by default.
    '''
    def __init__(self, page='https://en.wikipedia.org/wiki/Special:Random'):
        page = requests.get(page)
        self.page = page
        self.url = page.url
        self.status_code = page.status_code

    def get_html_element(self, element):
        ''' Get an HTML element like title, h1, p, etc... '''
        try:
            # Attempt to extract the element using a regular expression
            text = re.findall(r'<{name}[^>]*>(.*)(?:</{name})'.format(name=element),
                              self.page.text)[0]
        except Exception as e:
            print('Cannot find %s element on page' % element)
            raise e
        return text

def main():
    fire.Fire(WikiPage)

if __name__ == '__main__':
    main()