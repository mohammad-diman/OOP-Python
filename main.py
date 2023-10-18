class Pemain:
    def __init__(self, nama, umur, tinggi_badan):
        self.nama = nama
        self.umur = umur
        self.tinggi_badan = tinggi_badan


    def cetak_info(self):
        print(f"Nama: {self.nama}")
        print(f"Umur: {self.umur} tahun")
        print(f"Tinggi Badan: {self.tinggi_badan} cm")


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

# Membuat objek klub badminton
club = ClubBadminton("Club Badminton Centi")

# Menambahkan pemain dan pelatih ke klub
club.tambah_pelatih(pelatih)
club.tambah_pemain(pemain1)
club.tambah_pemain(pemain2)


# Menampilkan daftar pemain dan pelatih di klub
club.tampilkan_daftar_pelatih()
club.tampilkan_daftar_pemain()

tambah_pemain = input("ingin menambahkan pemain?(y/n): ")

if tambah_pemain.lower() == "y":
    nama = input("Masukkan nama pemain: ")
    umur = int(input("Masukkan umur pemain: "))
    tinggi_badan = int(input("Masukkan tinggi pemain (dalam cm): "))

    pemain_baru = Pemain(nama, umur, tinggi_badan)

    club.tambah_pemain(pemain_baru)
    print(f"{nama} telah di tambahkan ke dalam club")


kick_pemain = input("ingin mengeluarkan pemain?(y/n): ")

if kick_pemain.lower() == "y":
    club.tampilkan_daftar_pemain()

    kick_nama = input("Masukkan nama pemain yang akan di keluarkan: ")

    for pemain in club.daftar_pemain:
        if pemain.nama == kick_pemain:
            club.daftar_pemain.remove()
            print(f"{kick_nama} telah di keluarkan dari club.")
            break
    else:
        print(f"{kick_nama}telah keluar dari club")


lihat_daftar = input("lihat daftar pemain? (y/n): ")

if lihat_daftar.lower() == "y":
    club.tampilkan_daftar_pemain()

lihat_daftar = input("lihat daftar pelatih? (y/n): ")

if lihat_daftar.lower() == "y":
    club.tampilkan_daftar_pelatih()

else:
    print("Terima Kasih")
    