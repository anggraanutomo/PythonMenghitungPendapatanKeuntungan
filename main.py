# Kebutuhan Bahan Baku
bahanBaku = [
    {
        'Jenis Barang': 'Kain Katun',
        'Jumlah': 150,
        'Satuan': 'Meter',
        'Harga Satuan': 25000
    },
    {
        'Jenis Barang': 'Kain Keras',
        'Jumlah': 20,
        'Satuan': 'Meter',
        'Harga Satuan': 5000
    },
    {
        'Jenis Barang': 'Jarum mesin',
        'Jumlah': 2,
        'Satuan': 'Pack',
        'Harga Satuan': 15000
    },
    {
        'Jenis Barang': 'Benang jahit',
        'Jumlah': 30,
        'Satuan': 'Roll',
        'Harga Satuan': 20000
    },
    {
        'Jenis Barang': 'Benang obras',
        'Jumlah': 15,
        'Satuan': 'Roll',
        'Harga Satuan': 20000
    },
    {
        'Jenis Barang': 'Kancing',
        'Jumlah': 500,
        'Satuan': 'Pcs',
        'Harga Satuan': 700
    },
    {
        'Jenis Barang': 'Lubang kancing',
        'Jumlah': 500,
        'Satuan': 'Pcs',
        'Harga Satuan': 400
    }
]

# Kebutuhan pendukung
kebutuhanPendukung = [
    {
        'Jenis Kebutuhan': 'Upah tenaga kerja',
        'Jumlah': 15,
        'Satuan': 'Orang',
        'Harga Satuan': 200000
    },
    {
        'Jenis Kebutuhan': 'Biaya Listrik',
        'Jumlah': 1,
        'Satuan': 'Lumpsum',
        'Harga Satuan': 75000
    },
    {
        'Jenis Kebutuhan': 'Biaya Transportasi',
        'Jumlah': 1,
        'Satuan': 'Lumpsum',
        'Harga Satuan': 500000
    }
]

# Transaksi Penjualan
transaksi = [
    {
        'Bulan': 'Oktober',
        'Jumlah': 10
    },
    {
        'Bulan': 'Oktober',
        'Jumlah': 20
    },
    {
        'Bulan': 'Oktober',
        'Jumlah': 12
    },
    {
        'Bulan': 'November',
        'Jumlah': 18
    },
    {
        'Bulan': 'November',
        'Jumlah': 15
    },
    {
        'Bulan': 'Desember',
        'Jumlah': 25
    },
    {
        'Bulan': 'Desember',
        'Jumlah': 10
    },
    {
        'Bulan': 'Desember',
        'Jumlah': 12
    },
    {
        'Bulan': 'Desember',
        'Jumlah': 17
    }
]


# Fungsi untuk menghitung total_harga dari Harga Satuan x Jumlah
def hitung_total_harga(data):
    total = 0
    for item in data:
        total += item['Harga Satuan'] * item['Jumlah']
    return total


bahan_baku_total = hitung_total_harga(bahanBaku)
pendukung_total = hitung_total_harga(kebutuhanPendukung)

print("Total harga bahan baku: Rp", bahan_baku_total)
print("Total harga kebutuhan pendukung: Rp", pendukung_total)

# Menghitung Harga pokok produksi (HPP) total kebutuhan baku + total kebutuhan pendukung
hpp = bahan_baku_total + pendukung_total
print("Harga pokok produksi: Rp", hpp)

# Menghitung jumlah penjualan, pendapatan dan Keuntungan

harga_jual = 9000000  # misalkan harga jual 9.000.000
modal = 5000000  # misalkan modal 5.000.000

data_penjualan = {}

for transaksi_ in transaksi:
    bulan = transaksi_['Bulan']
    jumlah = transaksi_['Jumlah']

    if bulan in data_penjualan:
        data_penjualan[bulan]['Jumlah Penjualan'] += jumlah
    else:
        data_penjualan[bulan] = {'Jumlah Penjualan': jumlah}

for bulan, detail in data_penjualan.items():
    jumlah_penjualan = detail['Jumlah Penjualan']
    pendapatan = jumlah_penjualan * harga_jual
    modal = hpp * jumlah_penjualan
    keuntungan = pendapatan - modal
    detail['Pendapatan'] = pendapatan
    detail['Keuntungan'] = keuntungan

print("\n");
print("No | Bulan     | Jumlah Penjualan | Pendapatan | Keuntungan")
for index, (bulan, detail) in enumerate(data_penjualan.items()):
    print(index+1, " | ", bulan, " | ", detail['Jumlah Penjualan'],"              | ", detail['Pendapatan'], " | ", detail['Keuntungan'])
