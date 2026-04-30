class RemoteTv:
    def __init__(self,nama):
        self.nama = nama
        self.brightness = 0


    def naikkan_brightness(self):
        if self.brightness  < 10 :
            self.brightness += 1

    def turunkan_brightness(self):
        if self.brightness > 0:
            self.brightness -= 1

    def show(self):
        print(f"{self.nama} = {self.brightness}")
        

remoteA = RemoteTv("Remote A")
remoteB = RemoteTv("Remote B")

remoteA.naikkan_brightness()
remoteA.naikkan_brightness()
remoteA.naikkan_brightness()
remoteB.naikkan_brightness()
remoteA.show()
remoteB.show()

# Perbedaan Atribut dan Method 

#Atribut adalah data/variabel yang dimiliki oleh objek. contohnya :
# nama → menyimpan nama remote
# brightness → menyimpan tingkat kecerahan
# Atribut = menyimpan keadaan (state) objek

#Method adalah fungsi yang dimiliki oleh objek. contohnya :
# naikkan_brightness() → meningkatkan tingkat kecerahan
# turunkan_brightness() → menurunkan tingkat kecerahan
# show() → menampilkan nama dan tingkat kecerahan
# Method = menyimpan perilaku (behavior) objek

# Kesimpulan : Atribut menyimpan data tentang objek, sedangkan method menyimpan fungsi atau tindakan yang dapat dilakukan oleh objek.

# kenapa state bebeda karena setiap objek memiliki nilai atribut yang berbeda. Misalnya, remoteA memiliki brightness 3, sedangkan remoteB memiliki brightness 1. Ini menunjukkan bahwa setiap objek memiliki keadaan (state) yang unik berdasarkan nilai atributnya.


