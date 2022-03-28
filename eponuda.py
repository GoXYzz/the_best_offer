import requests
import webbrowser
from bs4 import BeautifulSoup
# pip install googlesearch-python
from googlesearch import search 

class PriceSearcher:
	"""Input name of the model you searching for and find the best offer in Serbia online"""
	def __init__(self, artikl):
		self.artikl = artikl
		
	def article_searcher(self):
		lista_linkova_google = search(artikl + ' eponuda')
		lista_cena = []
		lista_linkova_eponuda = []
		r = requests.get(lista_linkova_google[0])
		soup = BeautifulSoup(r.text, features='lxml')
		results = soup.find('div', {'class' : 'cene regular-prices'})
		for element in results:
			for stat in element.find_all('div', {'class' : 'c-table__row__price__real'}):
				lista_cena.append(stat.text)
			for a in element.find_all('a', href=True):
				lista_linkova_eponuda.append('https://www.eponuda.com' + a['href'])
		print("The best offer for " + artikl + " is  " + lista_cena[0] + " RSD.")
		prvi_link = lista_linkova_eponuda[0]
		webbrowser.open_new(prvi_link)

artikl = input("Enter the model: ")
new_search = PriceSearcher(artikl)
new_search.article_searcher()
