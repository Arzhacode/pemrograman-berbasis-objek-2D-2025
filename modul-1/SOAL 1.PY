#SOAL1_ARZHA DWI ANANDA A.W
class Manusia:
    def __init__(self, nama, umur, alamat):
        self.nama = nama
        self.umur = umur
        self.alamat = alamat

    def berjalan(self):
        return f"{self.nama} sedang berjalan."

    def berlari(self):
        return f"{self.nama} sedang berlari."

    # methodd untuk menampilkan
    def tampilkan_umur_dan_alamat(self):
        return f"Umur {self.nama}: {self.umur} tahun, Alamat: {self.alamat}"

# membuat objeknya
manusia1 = Manusia("Arzha", 20, "Jl. Telang No. 5")
manusia2 = Manusia("Bima", 20, "Jl. Raya Kamal. 10")
manusia3 = Manusia("Farhan", 20, "Jl. Kamal No. 12")
manusia4 = Manusia("Irsad", 20, "Jl. Telang No. 15")
manusia5 = Manusia("Rivqi", 20, "Jl. Graha No. 20")

#output an nyaa
print(manusia1.berjalan())
print(manusia1.tampilkan_umur_dan_alamat())

print(manusia2.berlari())
print(manusia2.tampilkan_umur_dan_alamat())

print(manusia3.berjalan())
print(manusia3.tampilkan_umur_dan_alamat())

print(manusia4.berlari())
print(manusia4.tampilkan_umur_dan_alamat())

print(manusia5.berjalan())
print(manusia5.tampilkan_umur_dan_alamat())
