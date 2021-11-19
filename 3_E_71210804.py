depan, tengah, belakang = list(input("Masukan daftar siswa :") .split(","))
a = depan.title()
b = tengah.title()
c = belakang.title()
print("\nDaftar Siswa : ['"+a+"', '"+b+"', '"+c+"']")
d = input("\nMasukkan siswa yang ingin ditambahkan : ")
e = d.title()
f = e.upper()
if (e == a) :
    print("\nSiswa atas nama" ,f, "sudah berada dalam daftar siswa")
elif (e == b) :
    print("\nSiswa atas nama" ,f, "sudah berada dalam daftar siswa")
elif (e == c) :
    print("\nSiswa atas nama" ,f, "sudah berada dalam daftar siswa")
else :
    print("\nHasil penambahan pada daftar siswa : ['"+a+"', '"+b+"', '"+c+"', '"+f+"']")
