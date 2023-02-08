
# menambahkan elemen - append
daftar_buku = ["heri potter", "jujur kasian", "gatotkaca", "bima satria"]
daftar_buku.append("legenda malin kundang")
print(daftar_buku )
print("\n")

print("-- dengan perulangan (pengolahan data )")
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])
print("\n")

# menampilkan dengan index tertentu
print("-- menampilkan dengan index tertentu")
print(daftar_buku[3])
print("\n")

# menghilangkan elemen - clear
print('-- menghilangkan elemen')
daftar_buku.clear()
print(daftar_buku)
print("\n")

#ganti elemen
print("-- ganti elemen {negeri bedebah di ganti matahari}")
daftar_buku = [ "negri bedebah", "negri ujung tanduk", "bumi", "bulan"]
daftar_buku[0] = "matahari"
print(daftar_buku)
print('\n')

#pop - mengambil elemen
daftar_buku = [ "negri bedebah", "negri ujung tanduk", "bumi", "bulan"]
print('daftar asli')
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])
print('\n- pop ---> mengambil elemen')
daftar_buku.pop()
# print(daftar_buku)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])
#pop -1
print('\n- pop -2')
daftar_buku.pop(-2)
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])


print('\n- perintah del')
print('\t\t\tdaftar asli')
daftar_buku = [ "negri bedebah", "negri ujung tanduk", "bumi", "bulan, matahari"]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print('\n - del[0]')
del daftar_buku[0]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

#list comperhension
print('\t== LIST COMPERHENSION ==')
print("perintah del dengan comperhension START:STOP")
del daftar_buku[0:-2]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])

print("perintah del dengan comperhension START:STOP:STEP")
del daftar_buku[0::2]
for i in range(0,len(daftar_buku)):
    print(daftar_buku[i])




