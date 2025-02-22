from Leitner_System_Project import *
import time

print("""
Leitner System Program

Operations:

1.Show the data
2.Show the terms
3.Add term
4.Delete term
5.Random term exercise


Press 'q' to leave the program.
""")

while True:
    Girdi=input("Please select an operation:")
    if Girdi=="q":
        print("Farewell...")
        break
    elif Girdi=="1":
        liste1.Listeyi_göster()
    elif Girdi=="2":
        liste1.Kelimeleri_göster()
    elif Girdi=="3":
        Terim=input("Term:")
        Anlamı=input("Meaning:")
        try:
            Sırası=int(input("Tier:"))
            if Sırası>5 or Sırası<1:
                print("Please enter a valid tier. (1-5)")
                continue
        except ValueError:
            print("Please enter a number.")
            continue
        kelime_yeni=kelime(Terim,Anlamı,Sırası)
        liste1.Terim_ekle(kelime_yeni)
    elif Girdi=="4":
        if not liste1.Check_data():
            print("There is no data in the list.")
        else:
            Silinecek=input("The term to be deleted:")
            onay=input(f"Delete {Silinecek}? (Y/N)")
            if onay.lower() == "y":
                liste1.Terim_sil(Silinecek)
            elif onay.lower() == "n":
                print(f"{Silinecek} will not be deleted.")
            else:
                print("Please select a valid operation.")
    elif Girdi=="5":
        liste1.Rastgele()
    else:
        print("Please enter a valid operation.")







