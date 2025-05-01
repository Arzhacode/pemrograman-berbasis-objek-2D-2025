# Soal 2 Arzha
class Pengiriman:
    def __init__(self, asal, tujuan):
        self.asal = asal
        self.tujuan = tujuan

    def estimasi_waktu(self):
        return 5  


class PengirimanDarat(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "jne":
            return 4
        elif self.maskapai.lower() == "tiki":
            return 5
        elif self.maskapai.lower() == "pos indonesia":
            return 6
        else:
            return 7


class PengirimanUdara(Pengiriman):
    def __init__(self, asal, tujuan, maskapai):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai

    def estimasi_waktu(self):
        if self.maskapai.lower() == "garuda":
            waktu = 2
        elif self.maskapai.lower() == "lion air":
            waktu = 3
        else:
            waktu = 4

        if self.tujuan.lower() != "indonesia":
            waktu += 3  

        return waktu


class PengirimanInternasional(Pengiriman):
    def __init__(self, asal, tujuan, maskapai, metode):
        super().__init__(asal, tujuan)
        self.maskapai = maskapai
        self.metode = metode.lower()  

    def estimasi_waktu(self):
        if self.metode == "darat":
            if self.maskapai.lower() == "jne":
                waktu = 4
            elif self.maskapai.lower() == "tiki":
                waktu = 5
            elif self.maskapai.lower() == "pos indonesia":
                waktu = 6
            else:
                waktu = 7
        elif self.metode == "udara":
            if self.maskapai.lower() == "garuda":
                waktu = 2
            elif self.maskapai.lower() == "lion air":
                waktu = 3
            else:
                waktu = 4
        else:
            waktu = 5  

        if self.tujuan.lower() != "indonesia":
            waktu += 3 

        return waktu


pengiriman1 = PengirimanInternasional("Jakarta", "Malaysia", "JNE", "darat")
pengiriman2 = PengirimanInternasional("Bandung", "Indonesia", "TIKI", "darat")
pengiriman3 = PengirimanInternasional("Surabaya", "Singapura", "Pos Indonesia", "darat")

pengiriman4 = PengirimanUdara("Jakarta", "Bali", "Garuda")
pengiriman5 = PengirimanUdara("Medan", "Surabaya", "Lion Air")
pengiriman6 = PengirimanUdara("Makassar", "Singapura", "Sriwijaya Air")

pengiriman_list = [pengiriman1, pengiriman2, pengiriman3, pengiriman4, pengiriman5, pengiriman6]

print("="*50)
print("  📦 INFO ESTIMASI PENGIRIMAN INTERNASIONAL 📦")
print("="*50)

for pengiriman in pengiriman_list:
    print(f"🌍 Dari: {pengiriman.asal}")
    print(f"📍 Tujuan: {pengiriman.tujuan}")
    print(f"🚚 Maskapai: {pengiriman.maskapai}")
    print(f"⏳ Estimasi Waktu: {pengiriman.estimasi_waktu()} hari")
    print("-"*50)
