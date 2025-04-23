import sqlite3
import datetime
import random

class kelime():
    def __init__(self,terim,anlamı,sırası):
        self.terim=terim
        self.anlamı=anlamı
        self.sırası=sırası
    def __str__(self):
        return "Kelime:{}\nAnlamı:{}\nSırası:{}".format(self.terim,self.anlamı,self.sırası)

class liste():
    def __init__(self):
        self.bağlantı_oluştur()
    def bağlantı_oluştur(self):
        self.bağlantı=sqlite3.connect("Liste.db")
        self.cursor=self.bağlantı.cursor()
        sorgu="""create table if not exists Liste (
        Terim TEXT COLLATE NOCASE,
        Anlamı TEXT COLLATE NOCASE,
        Sırası INT
        )"""
        self.cursor.execute(sorgu)
        self.bağlantı.commit()
    def bağlantı_kes(self):
        self.bağlantı.close()
    def Check_data(self):
        sorgu="select * from Liste"
        self.cursor.execute(sorgu)
        list=self.cursor.fetchall()
        return len(list)>0
    def Listeyi_göster(self):
        sorgu="select * from Liste"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("There is no data in the list.")
        else:
            for a in liste:
                print("Your list:")
                Veri=kelime(a[0],a[1],a[2])
                print("-----------------------------------------------")
                print(Veri)
    def Kelimeleri_göster(self):
        sorgu="select Terim from Liste"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("There is no data in the list.")
        else:
            for a in liste:
                print("Terms:")
                print(a)
    def Anlamları_göster(self,terim):
        sorgu="select Terim,Anlamı from Liste where Terim=?"
        self.cursor.execute(sorgu,(terim,))
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("There is no data in the list.")
        else:
            for a,b in liste:
                print(f"{a}={b}")
    def Terim_ekle(self,terim):
        sorgu="select * from Liste where Terim=? and Anlamı=? and Sırası=?"
        self.cursor.execute(sorgu,(terim.terim,terim.anlamı,terim.sırası))
        liste=self.cursor.fetchall()
        if len(liste)>0:
            print("This term already exists.")
        else:
            sorgu="insert into Liste values(?,?,?)"
            self.cursor.execute(sorgu,(terim.terim,terim.anlamı,terim.sırası))
            self.bağlantı.commit()
            print(f"{terim.terim} is added to the list")
    def Terim_sil(self,terim):
        sorgu="select * from Liste where Terim = ? COLLATE NOCASE"
        self.cursor.execute(sorgu,(terim,))
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("There is no such term.")
        else:
            sorgu="delete from Liste where Terim = ? COLLATE NOCASE"
            self.cursor.execute(sorgu,(terim,))
            self.bağlantı.commit()
            print(f"{terim} is deleted.")
    def Sırayı_artır(self,terim,anlamı):
        sorgu="select * from Liste where Terim=? and Anlamı=?"
        self.cursor.execute(sorgu,(terim,anlamı,))
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("The term or the meaning you have entered is wrong.")
            liste1.Doğrusu(terim,anlamı)

        else:
            sıra=liste[0][2]
            sıra+=1
            if sıra==6:
                print(f"{terim} is already at the highest tier.")
                sıra-=1
            else:
                sorgu="update Liste set Sırası=? where Terim=? and Anlamı=?"
                self.cursor.execute(sorgu,(sıra,terim,anlamı))
                self.bağlantı.commit()
                print(f"{terim} kelimesinin sırası artırıldı.\nYeni Sırası:{sıra}")
    def Sırayı_düşür(self,terim):
        sorgu="select * from Liste where Terim=? COLLATE NOCASE"
        self.cursor.execute(sorgu,(terim,))
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("There is no such term.")
        else:
            sıra=liste[0][2]
            sıra-=1
            if sıra==0:
                print(f"{terim} is already at the lowest tier.")
                sıra+=1
            else:
                sorgu="update Liste set Sırası=? where Terim=?"
                self.cursor.execute(sorgu,(sıra,terim))
                self.bağlantı.commit()
                print(f"It's new tier: {sıra}")


    def Rastgele(self):
        sorgu="select Terim, Anlamı from Liste"
        self.cursor.execute(sorgu)
        liste=self.cursor.fetchall()
        if len(liste)==0:
            print("There is no data in the list.")
        else:
            rastgele=random.choice(liste)
            terim,anlamı=rastgele
            print("Your term:"+ terim)
            anlam_kontrolü=input("The meaning of the term:")
            if anlam_kontrolü.lower()==anlamı.lower():
                print("Correct.")
                liste1.Sırayı_artır(terim,anlamı)
            else:
                print("Wrong.")
                self.Doğrusu(terim,anlamı)
    def Doğrusu(self,terim,anlamı):
        sorgu="select Terim,Anlamı from Liste where Terim=?"
        self.cursor.execute(sorgu,(terim,))
        liste=self.cursor.fetchall()
        if liste:
            doğru=liste[0][0]
            print(f"Correction: {doğru}={liste[0][1]}")
            print("Decreasing tier..")
            self.Sırayı_düşür(doğru)
        else:
            sorgu = "select Terim,Anlamı from Liste where Terim=?"
            self.cursor.execute(sorgu, (terim,))
            liste = self.cursor.fetchall()
            if liste:
                doğru=liste[0][0]
                print(f"Correction: {doğru}={liste[0][1]}")
                print("Decreasing tier..")
                self.Sırayı_düşür(doğru)

liste1=liste()
