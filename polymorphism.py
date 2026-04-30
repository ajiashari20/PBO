class Kendaraan:
    def __init__(self, merk, warna, roda, mesin):
        self.merk = merk
        self.warna = warna
        self.roda = roda
        self.mesin = mesin

    def nyalakan_mesin(self):
        print(f"{self.merk}: Mesin dinyalakan")

    def akselerasi(self):
        print(f"{self.merk}: Akselerasi umum")

    def rem(self):
        print(f"{self.merk}: Mengerem")

    # Overloading sederhana (pakai parameter opsional)
    def isi_bahan_bakar(self, volume=None, harga=None):
        if volume is not None:
            print(f"{self.merk}: Isi {volume} liter bensin")
        elif harga is not None:
            print(f"{self.merk}: Isi bensin senilai Rp{harga}")
        else:
            print("Masukkan volume atau harga!")

class Mobil(Kendaraan):
    def __init__(self, merk, warna, jumlah_kursi):
        super().__init__(merk, warna, roda=4, mesin="Bensin")
        self.jumlah_kursi = jumlah_kursi

    # Overriding
    def akselerasi(self):
        print(f"{self.merk}: Injak pedal gas")

    def nyalakan_wiper(self):
        print(f"{self.merk}: Wiper menyala")

    def nyalakan_ac(self):
        print(f"{self.merk}: AC menyala")

class SepedaMotor(Kendaraan):
    def __init__(self, merk, warna, tipe_starter, jumlah_shock):
        super().__init__(merk, warna, roda=2, mesin="Bensin")
        self.tipe_starter = tipe_starter
        self.jumlah_shock = jumlah_shock

    # Overriding
    def akselerasi(self):
        print(f"{self.merk}: Tarik tuas gas")

    def starter(self):
        print(f"{self.merk}: Starter {self.tipe_starter}")

mobil = Mobil("Mobil", "Hitam", 5)
motor = SepedaMotor("Motor", "Merah", "Electric", 2)

mobil.nyalakan_mesin()
mobil.akselerasi()
mobil.nyalakan_wiper()
mobil.isi_bahan_bakar(volume=20)

print()

motor.nyalakan_mesin()
motor.akselerasi()
motor.starter()
motor.isi_bahan_bakar(harga=50000)