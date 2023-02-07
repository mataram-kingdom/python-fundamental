
# menambahkan elemen - append
daftar_buku = ["heri potter", "jujur kasian", "gatotkaca", "bima satria"]
daftar_buku.append("legenda malin kundang")
print(daftar_buku )

print("-- dengan perulangan (pengolahan data ) =========")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

# menampilkan dengan index tertentu
print(" -- menampilkan dengan index tertentu")
print(daftar_buku[3])


# menghilangkan elemen - clear
print(' -- menghilangkan elemen')
daftar_buku.clear()
print(daftar_buku)

