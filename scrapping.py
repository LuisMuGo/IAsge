import mechanicalsoup
import csv
import os

import time

class scrapping():
    #String word
    #String base
    
    def __init__(self,word) -> None:
        self.base = "https://www.amazon.es/"  #Link inicial
        self.word = word                      #Palabra
        self.pageLinks = []                   #Links de las webs
        self.reviewLinks = []                 #Links review
        self.text_comments = []
        self.stars_comments = []
        dir = os.path.abspath(__file__)
        self.parent = os.path.dirname(dir)

    def getLinksPage(self,page:int):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup') #Creamos el browser
        url = f"{self.base}s?k={self.word}&page={page}" #URL DE WEB
        browser.open(url) #Abrimos el browser
        print(f"Url: {browser.url}")
        #Obtenemos la pagina
        page = browser.page #Obtenemos web
        
        #Obtenemos los spans que contienen los links
        spans = page.find_all("span", {"class": "rush-component"}) #Buscamos spans contenedores
        print(f"Hola")
        for span in spans:
            #Obtenemos los links
            links = span.find_all("a",{"class":"a-link-normal s-no-outline"}) #Buscamoss links
            for link in links:
                href = link['href']
                href = self.base + href
                self.pageLinks.append(href) #Gardamos datos en una tabla
        #Cerramos objeto browser
        browser.close()
        pass

    def getAllReviewLinks(self):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')
        for i in range(len(self.pageLinks)):
            url = self.pageLinks[i]
            browser.open(url)
            page = browser.page
            links = page.find_all("a",{"class":"a-link-emphasis a-text-bold"})
            if(len(links) > 0 ):
                if len(self.reviewLinks) > 20:
                    print("finish")
                    break
                link = links[0]['href']
                link = self.base + link
                self.reviewLinks.append(link)
            pass
        browser.close()
        # Devolvemos tabla con links
    
    def writeCsv(self):
        commentList = []
        disalowed_character = "!,?.)(':¿¡*“”"
        print(f"Stars Reg: {len(self.stars_comments)} - Txt Reg: {len(self.text_comments)}")

        for i in range(len(self.text_comments)):
            commentList.append([])
            commentList[i].append(self.text_comments[i].replace("\"", "").replace(",", "").lower())
            commentList[i].append(self.stars_comments[i].replace("\"", "").replace(",", "").replace("0","").lower())
        
        with open(os.path.join(self.parent,"comments.csv"), 'w', encoding="utf-8") as file:
           for i in range(len(commentList)):
                for character in disalowed_character:
                    commentList[i][0] = commentList[i][0].replace(character,"")
                txt = "\"" + commentList[i][0] + "\",\""+ commentList[i][1] + "\"\n"
                file.write(txt)
        
        print("finish")
        
        
    def getComments(self):
        browser = mechanicalsoup.StatefulBrowser(user_agent='MechanicalSoup')     #Creamos el browser
        for link in self.reviewLinks:
            print("-----------------------")
            print(link)
            #Abrimos el browser
            for pageNum in range(1, 10):
                pages = f"&pageNumber={pageNum}"
                host = link + pages                                                            #URL DE WEB
                browser.open(host) 
                print(host)
                page = browser.page
                sections = page.find_all("div", {"class": "a-section review aok-relative"})
                if (len(sections) < 1):
                    print("ROTO")
                    break
                for section in sections:
                    spans = section.find_all("span", {"class": "a-size-base review-text review-text-content"})
                    stars = section.find_all("span", {"class": "a-icon-alt"})
                    #print(f"---------------\n --> \n {section}")
                    if(len(spans) > 0 and len(stars) > 0):
                        span = spans[0].text
                        star = stars[0].text
                        span = span.replace("\n","").replace("<span class=a-size-base review-text review-text-content data-hook=review-body>", "")
                        if ("video" in span or "img" in span or "no se ha podido cargar el contenido multimedia" in span):
                            print("VIDEO / img error:")
                        else:
                            star = star.replace("<span class=\"a-icon-alt\">", "").replace(" de 5 estrellas","")
                            self.stars_comments.append(star)
                            self.text_comments.append(span.replace("<span>", "").replace("</span>", "").replace("<br/>", ""))
        browser.close()
    
    def getPageLinks(self):
        return self.pageLinks 
    
    def getReviewLinks(self):
        return self.reviewLinks