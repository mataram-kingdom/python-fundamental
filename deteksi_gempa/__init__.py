
def ekstraksi_data():
    hasil = dict()
    hasil['tanggal'] = '09 februari 2023'
    hasil['waktu'] = '23:57:12 WIB'
    hasil['magnitudo'] = '3.0'
    hasil['radius'] = '8 km'
    hasil['lokasi'] = '2.54 LS - 140.68 BT'
    hasil['pusat'] = 'Pusat gempa berada di darat 4 km BaratDaya Kota Jayapura'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Kota Jayapura'
    return hasil


def tampilkan_data(result):
    print("gempa berdasarkan bmkg")
    print(f'tanggal {result["tanggal"]}')
    print(f'waktu {result["waktu"]}')
    print(f'magnitudo {result["magnitudo"]}')
    print(f'radius {result["radius"]}')
    print(f'loc {result["lokasi"]}')
    print(f'pusat {result["pusat"]}')
    print(f'ket {result["dirasakan"]}')
