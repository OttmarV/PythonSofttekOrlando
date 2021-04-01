"""
Cuando descargamos una web page desde el browser, se descarga un plain text formateado como HTML = Hypertext Markup Language.
HTML le dice al browser como ver el web page.
Para hacer un parse del HTML, se utiliza Beautiful Soup

Web pages are plaintext files formatted as HTML.
HTML can be parsed with the BeautifulSoup module.
BeautifulSoup is imported with the name bs4.
Pass the string with the HTML to the bs4.BeautfiulSoup() function to get a Soup object.
The Soup object has a select() method that can be passed a string of the CSS selector for an HTML tag.
You can get a CSS selector string from the browser's developer tools by right-clicking the element and selecting Copy CSS Path.
The select() method will return a list of matching Element objects.

"""
import bs4
import requests

res = requests.get("https://en.wikipedia.org/wiki/Lou_Spence")
print(res.status_code)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, features="html.parser")

elems = soup.select("#mw-content-text > div.mw-parser-output > table > tbody > tr:nth-child(6) > td") #el selector es un path de CSS
print(elems)
print(elems[0])
print(elems[0].text) # en el ejercicio de udemy, lo que se quiere se encuentra en el elemento 1
print(elems[0].text.strip()) #eliminamos espacios
