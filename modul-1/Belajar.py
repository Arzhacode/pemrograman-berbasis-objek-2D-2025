#ARZHA DWI AAW 24_062
class mahaasiswa: 
def __init__(self, nama, nim, kelas, jenis_kelamin, jurusan): 
     self.nama = nama 
     self.nim = nim 
     self.kelas = kelas 
     self.jenis_kelamin = jenis_kelamin 
     self.jurusan = jurusan 

def perkenalan(self): 
    print("Halo Nama Saya:", self.nama, "\nNIM:", 
          self.nim,  "\nkelas:",self.kelas, "\nJurusan:", self.jurusan,  "\ndan saya", self.jenis_kelamin, "\n")

mahasiswa1 = mahaasiswa ("Arza", "12345678", "2017A", "Laki-laki", "Sistem Informaasi") 
mahasiswa2 = mahaasiswa ("Irsad", "23832823", "2014b", "Laki-laki" "Teknik Informatika") 
mahasiswa3 = mahaasiswa ("Apan", "342242423", "2017D", "Laki-laki", "Teknik Industri") 
mahasiswa4 = mahaasiswa ("Bima", "4232424", "2017E", "perempuan", "Manajemen Informatika") 
mahasiswa5=  mahaasiswa ("Kiki", "4232412", "2011T", "Perempuan", "AKutansi")

mahasiswa1.perkenalan()
mahasiswa2.perkenalan()
mahasiswa3.perkenalan()
mahasiswa4.perkenalan()
mahasiswa5.perkenalan()