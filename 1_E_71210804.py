print("===== Kalkulator Akar dan Pangkat =====")
print("Pilihan menu :")
print("1. Pangkat 2 (Kuadrat)")
print("2. Pangkat 3 (Kubik)")
print("3. Akar Kuadrat")
menu = int(input("Masukan menu yang ingin anda pilih: "))
if (menu >=1) and (menu <= 2) :
    bilangan = int(input("Masukkan bilangan yang ingin dipangkatkan :"))
    if menu == 1:
        kuadrat = (bilangan**2)
        print("Hasil dari pemangkatan bilangan", (bilangan), "dengan 2 (Kuadrat) adalah", kuadrat)
    elif menu == 2:
        kubik = (bilangan**3)
        print("Hasil dari pemangkatan bilangan", (bilangan), "dengan 3 (Kubik) adalah", kubik)
elif (menu == 3) : 
     bilangan = int(input("Masukkan bilangan yang ingin diakarkan :"))
     akar = (bilangan**0.5)
     print("Hasil akar kuadrat dari bilangan", (bilangan), "adalah", akar)
else :
    print("Pilihan menu yang dimasukkan tidak sesuai!")