import mechanicalsoup

class scrapping():
    #String word
    #String base
    def __init__(self,word) -> None:
        self.base = "https://www.amazon.es/"                                      #Link inicial
        self.word = word                                                          #Palabra
        self.pageLinks = []                                                       #Links de las webs

    def getLinksPage(self,page:int):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')     #Creamos el browser
        url = f"{self.base}s?k={self.word}&page={page}"                           #URL DE WEB
        browser.open(url)                                                         #Abrimos el browser
        print(f"Url: {browser.url}")
        #Obtenemos la pagina
        page = browser.page                                                       #Obtenemos web
        #Obtenemos los spans que contienen los links
        spans = page.find_all("span", {"class": "rush-component"})                #Buscamos spans contenedores
        for span in spans:
            #Obtenemos los links
            links = span.find_all("a",{"class":"a-link-normal s-no-outline"})     #Buscamoss links
            for link in links:
              href = link['href']
              href = self.base + href
              self.pageLinks.append(href)                                         #Gardamos datos en una tabla
        #Cerramos objeto browser
        browser.close()
        pass

    def getPageLinks(self):
        return self.pageLinks