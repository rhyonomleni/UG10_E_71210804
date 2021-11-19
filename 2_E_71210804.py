suhu = float (input("Masukan suhu tubuh Anda : "))
if suhu > 50 : 
    print("Anda bukan Manusia :)") 
elif suhu < 32 : 
    print("Anda kedinginan! Silahkan cari sesuatu yang hangat")
elif 50 >= suhu > 37.5 :
    print("Anda demam! Jangan bepergian ke tempat fasilitas Umum")
elif 37.5 >= suhu > 32 :
    print("Suhu Anda normal")