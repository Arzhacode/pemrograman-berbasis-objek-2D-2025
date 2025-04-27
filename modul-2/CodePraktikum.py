# Modul 2 PBO Arzha
class Mahasiswa:
    total_mahasiswa = 0

    def __init__(self, nama, nim, prodi, kampus):
        self.nama = nama
        self.nim = nim
        self.prodi = prodi
        self.kampus = kampus  
        self.daftar_matkul = []

        if not self.validasi_nim(nim):
            print(f"! NIM {nim} tidak valid (harus 10 digit dan diawali '23')")
            print("-" * 60)

        Mahasiswa.total_mahasiswa += 1

    def tambah_matkul(self, matkul):
        if len(self.daftar_matkul) >= 8:
            print(f"! {self.nama} sudah mengambil maksimal 8 mata kuliah")
            return False
        self.daftar_matkul.append(matkul)

    def tampilkan_info(self):
        print("\n" + "=" * 60)
        print(f"NAMA   : {self.nama.upper()}")
        print(f"NIM    : {self.nim}")
        print(f"PRODI  : {self.prodi.upper()}")
        print(f"KAMPUS : {self.kampus.nama.strip()}")
        print("\nMATA KULIAH YANG DIAMBIL:")
        for i, matkul in enumerate(self.daftar_matkul, 1):
            valid = matkul.validasi_sks(matkul.sks)
            status = "" if valid else " (SKS TIDAK VALID)"
            print(f"{i}. {matkul.nama} - {matkul.sks} SKS{status}")
        print("-" * 60)

    @classmethod
    def jumlah_mahasiswa(cls):
        print(f"\nTOTAL MAHASISWA: {cls.total_mahasiswa}")

    @staticmethod
    def validasi_nim(nim):
        return len(str(nim)) == 10 and str(nim).startswith('23')


class MataKuliah:
    def __init__(self, kode, nama, sks):
        self.kode = kode
        self.nama = nama
        self.sks = sks

    @staticmethod
    def validasi_sks(sks):
        return sks in {2, 3}


class Kampus:
    def __init__(self, nama, alamat):
        self.nama = nama
        self.alamat = alamat

        if not self.validasi_nama(nama):
            print(f"Nama kampus '{nama}' tidak valid")

    def tampilkan_info(self):
        print("\n" + "=" * 50)
        print("INFORMASI KAMPUS".center(50))
        print("=" * 50)
        print(f"Nama   : {self.nama}")
        print(f"Alamat : {self.alamat}")
        print(f"Status : {'VALID' if self.validasi_nama(self.nama) else 'TIDAK VALID'}")
        print("=" * 50)

# untuk cek nama kampusnya itu hanya huruf dan spasii
    @staticmethod
    def validasi_nama(nama):
        return all(char.isalpha() or char.isspace() for char in nama)

# saya pakai 2 kampus sbg contoh
kampus_utm = Kampus("Universitas Trunodjoyo", "Madura")
kampus_unair = Kampus("Universitas Airlangga", "Surabaya")

# matkulnyaa
matkuls = [
    MataKuliah("MK001", "Pemrograman Berbasis Objek", 3),
    MataKuliah("MK002", "BINGGRIS", 3),
    MataKuliah("MK003", "ALPRO", 3),
    MataKuliah("MK004", "Basis Data", 4),
    MataKuliah("MK005", "PBW", 3),
    MataKuliah("MK006", "DMJ", 3),
    MataKuliah("MK007", "APB", 2),
    MataKuliah("MK008", "Logika Engineering", 5)
]

# mahasiswa yang dimasukkan kedalam list mahasiswas
mahasiswas = [
    Mahasiswa("ARZHA", "2312345678", "Teknik Informatika", kampus_utm),
    Mahasiswa("FARHAN", "2311111111", "Sistem Informasi", kampus_unair),
    Mahasiswa("IRSAD", "2322222222", "Teknik Komputer", kampus_utm),
    Mahasiswa("KIKI", "2333333333", "Sistem Informasi", kampus_unair),
    Mahasiswa("JOIS", "2344444444", "Teknik Informatika", kampus_utm),
    Mahasiswa("RIZKI", "2355555555", "Teknik Komputer", kampus_unair),
    Mahasiswa("ANUN", "2366666666", "Teknik Komputer", kampus_utm)
]

# saya pakai cara manual untuk menambahkan matkul agar gampang dipahamiii
mahasiswas[0].tambah_matkul(matkuls[7])  # ARZHA
mahasiswas[0].tambah_matkul(matkuls[1])
mahasiswas[0].tambah_matkul(matkuls[2])
mahasiswas[0].tambah_matkul(matkuls[3])
mahasiswas[0].tambah_matkul(matkuls[4])

mahasiswas[1].tambah_matkul(matkuls[2])  # FARHAN
mahasiswas[1].tambah_matkul(matkuls[3])
mahasiswas[1].tambah_matkul(matkuls[4])
mahasiswas[1].tambah_matkul(matkuls[1])

mahasiswas[2].tambah_matkul(matkuls[5])  # IRSAD
mahasiswas[2].tambah_matkul(matkuls[6])
mahasiswas[2].tambah_matkul(matkuls[0])
mahasiswas[2].tambah_matkul(matkuls[1])

mahasiswas[3].tambah_matkul(matkuls[7])  # KIKI
mahasiswas[3].tambah_matkul(matkuls[2])
mahasiswas[3].tambah_matkul(matkuls[3])
mahasiswas[3].tambah_matkul(matkuls[1])

mahasiswas[4].tambah_matkul(matkuls[3])  # JOIS
mahasiswas[4].tambah_matkul(matkuls[4])
mahasiswas[4].tambah_matkul(matkuls[1])
mahasiswas[4].tambah_matkul(matkuls[2])

mahasiswas[5].tambah_matkul(matkuls[5])  # RIZKI
mahasiswas[5].tambah_matkul(matkuls[6])
mahasiswas[5].tambah_matkul(matkuls[7])
mahasiswas[5].tambah_matkul(matkuls[4])

mahasiswas[6].tambah_matkul(matkuls[0])  # ANUN
mahasiswas[6].tambah_matkul(matkuls[1])
mahasiswas[6].tambah_matkul(matkuls[2])
mahasiswas[6].tambah_matkul(matkuls[3])

print("\n" + "=" * 60)
print("LAPORAN DATA MAHASISWA".center(60))
print("=" * 60)
for mahasiswa in mahasiswas:
    mahasiswa.tampilkan_info()

kampus_utm.tampilkan_info()
kampus_unair.tampilkan_info()

Mahasiswa.jumlah_mahasiswa()