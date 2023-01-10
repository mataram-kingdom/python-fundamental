# sekuensial
print('ibu berkata, "pergi ke toko"')
print('budi menjawab, "baik bu apa yang harus saya beli di toko" ')
print('ibu menjawab, "beli satu botol susu, dan jika ada telur beli 6"')
print("budi berangkat ke toko ")
print("budi mulai berbelanja\n\n")

# percabangan
jumlah_telur = 5
jumlah_botol_susu = 5
print("budi menegecek di warung apakah ada susu")
if jumlah_botol_susu > 0 :
    print("budi mengecek harga nya dan ternyata uang nya cukup")
    if jumlah_telur > 0:
        print("budi membeli 6 botol susu")
    else:
        print("budi membeli 1 botol susu")
else:
    print("budi tidak jadi membeli susu")

print("budi pulang ke rumah ")
print("budi menyerahkan belanja ke ibu")

print("program selesai")