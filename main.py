class Pemain:
    def __init__(self, nama, umur, tinggi_badan):
        self.nama = nama
        self.umur = umur
        self.tinggi_badan = tinggi_badan
        self.poin = 0

    def cetak_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")
        print(f"Tinggi Badan: {self.tinggi_badan} cm")
        print(f"Total Poin: {self.poin} poin")

    def tambah_poin(self, poin):
        self.poin += poin


class Pelatih:
    def __init__(self, nama, prestasi) -> None:
        self.nama = nama
        self.prestasi = prestasi

    def cetak_info(self):
        print(f"Nama: {self.nama}")
        print(f"Prestasi: {self.prestasi}")    

class ClubBadminton:
    def __init__(self, nama_club):
        self.nama_club = nama_club
        self.daftar_pelatih = []
        self.daftar_pemain = []

    def tambah_pelatih(self, pelatih):
        self.daftar_pelatih.append(pelatih)

    def tambah_pemain(self, pemain):
        self.daftar_pemain.append(pemain)

    def tampilkan_daftar_pelatih(self):
        print(f"Daftar Pelatih {self.nama_club}:")
        for pelatih in self.daftar_pelatih:
            pelatih.cetak_info()
            print("-" * 20)

    def tampilkan_daftar_pemain(self):
        print(f"Daftar Pemain {self.nama_club}:")
        for pemain in self.daftar_pemain:
            pemain.cetak_info()
            print("-" * 20)


#Membuat objek Pelatih
pelatih = Pelatih("Taufik Hidayat", "Meraih medali emas dalam nomor tunggal putra di Olimpiade Athens 2004. Juara di All England Championships, salah satu turnamen bulu tangkis tertua dan paling bergengsi di dunia. Meraih prestasi di Kejuaraan Dunia bulu tangkis, meskipun mungkin tidak memenangkan gelar tunggal dunia. Meraih banyak gelar nasional dan prestasi dalam berbagai turnamen nasional Indonesia.")            

# Membuat objek pemain
pemain1 = Pemain("Anjani", 20, 170)
pemain2 = Pemain("Diman", 22, 175)

# Membuat objek klub bulu tangkis
club = ClubBadminton("Club Badminton Centi")

# Menambahkan pemain dan pelatih ke klub
club.tambah_pelatih(pelatih)
club.tambah_pemain(pemain1)
club.tambah_pemain(pemain2)


# Menampilkan daftar pemain dan pelatih di klub
club.tampilkan_daftar_pelatih()
club.tampilkan_daftar_pemain()

# Menambahkan poin untuk pemain
pemain1.tambah_poin(10)
pemain2.tambah_poin(5)

# Menampilkan informasi pemain setelah penambahan poin
print("\nSetelah penambahan poin:")
club.tampilkan_daftar_pemain()