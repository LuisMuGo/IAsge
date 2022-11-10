import csv

from langdetect import detect


class ia():
    
    def __init__(self) -> None:
        self.reviews = []
    
    def readAndClean(self):
        with open('C:/Users/luism/Desktop/comments_bueno.csv', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                    language = detect(row[0])
                    if language == "es" and len(row[0])>0:
                        self.reviews.append(row)
        for review in self.reviews:
            print(len(review))
    
    