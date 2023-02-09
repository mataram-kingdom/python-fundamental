"""
aplikasi deteksi gempa terkini
"""
from deteksi_gempa import tampilkan_data, ekstraksi_data

# 09 Februari 2023, 23:57:12 WIB
# 3.0
# 8 km
# 2.54 LS - 140.68 BT
# Pusat gempa berada di darat 4 km BaratDaya Kota Jayapura
# Dirasakan (Skala MMI): II Kota Jayapura


if __name__ == '__main__':
    print("aplikasi utama")
    result = ekstraksi_data()
    tampilkan_data(result)
