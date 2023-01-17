
jumlah_buku = 10
print(f'ibu berkata, baca semua buku mu')

total_baca = 0

buku_yang_paham = 0
print(f'jumlah buku yang sudah dipahami = {buku_yang_paham}')

while total_baca < jumlah_buku * 2:
    total_baca = total_baca + 1
    if buku_yang_paham == 9:
        print(f'buku ke {buku_yang_paham + 1} belum paham')
    else:
        buku_yang_paham = buku_yang_paham + 1
        print(f'buku ke {buku_yang_paham} sudah dibaca dan dipahami')

print(f"jumlah buku yang dibaca dan dipahami {buku_yang_paham}")
if buku_yang_paham == jumlah_buku:
    print(f'bu, semua buku sudah saya baca dan saya pahami')
else:
    print(f"tidak semua buku dapat saya pahami bu")
