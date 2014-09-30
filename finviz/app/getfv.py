from lxml import html
import requests

page = requests.get('http://finviz.com')
tree = html.fromstring(page.text)

print tree
