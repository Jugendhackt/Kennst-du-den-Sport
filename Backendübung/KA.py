import sqlite3
import random
con = sqlite3.connect("../daten.db")
cur = con.cursor()
def fragenvon(kategorie):
    quizfragen=[]
    if kategorie == "": 
        for row in cur.execute('SELECT * fROM fRAGEN'):
            text=row[0]
            loesung=row[1]
            falsch=row[2:5]
            frage={}
            frage['text']=text
            frage['loesung']=loesung
            frage['falsch']=falsch
            quizfragen.append(frage)
    else:
        for row in cur.execute('SELECT * fROM fRAGEN WHERE KATEGORIE ="'+kategorie+'"'):
            text=row[0]
            loesung=row[1]
            falsch=row[2:5]
            frage={}
            frage['text']=text
            frage['loesung']=loesung
            frage['falsch']=falsch
            quizfragen.append(frage)
    if len(quizfragen)<10:
        quizfragen = fragenvon("")
    UpdatedList = random.sample(quizfragen, 10)
    return UpdatedList
print(fragenvon("Golf"))
 

    