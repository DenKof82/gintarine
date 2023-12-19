from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):

    def __init__(self):
        super().__init__()
        self.base_url = base_url
        self.page_url = page_url
        self.link = set


    def handle_starttag(self, tag, attrs):
        # print(tag)
        if tag == "a":
            for (attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin()


    #when call HTMLParser feed(), this funktion is called when it encounters an opening tag <a>
    def handle_starttag(selfself, tag, attrs):
        if tag == "a":
            for (attribute, value) in attrs:
                if attribute == "href":
                    url = parse.urljoin(self.base_url, value)
                    self.link.add(url)


    def error(self, mesaage):
        pass

#finder = LinkFinder()
#finder.feed('<html><head><title>Test</title></head>'
           # '<body><h1>Parse me!</h1></body></html')
