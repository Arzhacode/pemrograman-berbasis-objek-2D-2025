#SOAL2_ARZHA DWI ANANDA A.W
class Mahasiswa:
    def __init__(self, nama, nim, jurusan, alamat):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.alamat = alamat
    
    def tampilkan_info(self):
        print("Nama    :", self.nama)
        print("NIM     :", self.nim)
        print("Jurusan :", self.jurusan)
        print("Alamat  :", self.alamat)
        print("-" * 30)

mahasiswa_list = []

# looping nyaa
for i in range(5):
    print(f"Masukkan data mahasiswa ke-{i+1}:")
    nama = input("Nama       : ")
    nim = input("NIM        : ")
    jurusan = input("Jurusan    : ")
    alamat = input("Alamat     : ")
    
    mahasiswa = Mahasiswa(nama, nim, jurusan, alamat)
    mahasiswa_list.append(mahasiswa)
    print()

# Menampilkan informasi semua mahasiswa
print("Informasi Mahasiswa:")
for mahasiswa in mahasiswa_list:
    mahasiswa.tampilkan_info()
