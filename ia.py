import os
import pandas as pd
import numpy as np
class ia():
    
    def __init__(self) -> None:
        # Input  - > Comentarios  | Var X
        # Output - > Sentimientos | Var y
        # Nota: Los datos de input estan desbalancedos
        path = os.path.join(os.path.dirname(os.path.abspath(__file__)),"comments_pruebas.csv")
        print(path)
        df = pd.read_csv(path)
        print(df)
        print(df.value_counts("sentiment"))    



        # Importamos el divisor de datos
        from sklearn.model_selection import train_test_split
        #Dividimos data para entrenar y para testear
                                        #DF
        train, test = train_test_split(df,test_size=0.20,random_state=42)
        #Separamos en Input(X) y Output(Y) 
        train_x, train_y = train['review'],train['sentiment']
        test_x,  test_y  = test['review'] ,test['sentiment']

        #Transformamos texto a data numerica (Vectores)
            #Usando tecnica (Bag of Words) - (Bolsa de palabras)

        #Tecnica Tfidf -> Busca palabras representativas y relevantes en cada review.
        from sklearn.feature_extraction.text import TfidfVectorizer

        tfidf = TfidfVectorizer(max_features=3600) # Establecemos en maximo 80 palabras mas relevantes
        #Busca parametros ideales para nuestra data y aplicarlos
            #Transforma Str a Double
        train_x_vector = tfidf.fit_transform(train_x)    
        test_x_vector  = tfidf.fit_transform(test_x)

        #Modelo con aprendizaje supervisado en clasificación
        from sklearn.linear_model import LogisticRegression
        lr = LogisticRegression()
        print("Entrenando modelo...")
        lr.fit(train_x_vector,train_y)
        print("Modelo entrenado")
        print("Testeando modelo...")
        sc = lr.score(test_x_vector,test_y)
        print(f"Testeo finalizado con resultado = {round(sc*100,2)}% de aciertos")
        
        while(True):
            imp = input("Frase : ")
            if(imp == "-1"):
                break
            #Busca parametros ideales para nuestra data y aplicarlos
                #Transforma Str a Double
            
            dto = tfidf.transform([imp])
            
            result = lr.predict(dto)
            print(result)
            pass