from tabulate import tabulate
import math

data = [
    {"Bulan":"Bulan", "Pemasukan":"Pemasukan", "Pengeluaran":"Pengeluaran", "Sisa_uang":"Sisa_uang", "Tabungan":"Tabungan"},
    {"Bulan":"Januari", "Pemasukan":int(), "Pengeluaran":int(), "Sisa_uang":int(),"Tabungan":int() }
]

def buatkey():  # Fungsi untuk input kolom baru
    tambah_key = input("Buat Kolom Baru: ")
    return tambah_key


def lihatdata(): # Fungsi untuk melihat table keseluruhan
    print(tabulate(data, headers="firstrow", tablefmt="grid",
                numalign="right", stralign="left"))

def masukankey(): # Fungsi untuk memasukan key dari sebuah kolom
    enter_key = input("Masukan kolom (Bulan/Pemasukan/Pengeluaran/Sisa_uang perhatikan juga penggunaan huruf kapital!!): ")
    return enter_key

def lihatkey(): # Fungsi untuk melihat data pada kolom dalam bentuk table
    
        masukan_key=masukankey()
        key=[{masukan_key:row[masukan_key]}for row in data]
        print(tabulate(key,headers= "firstrow", tablefmt="grid",
                numalign="right", stralign="left"))
    

def input_bulan(): # Fungsi untuk input data baru pada kolom bulan
        bulan_baru = input("Masukan Nama Bulan: ")
        list_bulan_baru ={"Bulan":bulan_baru, "Pemasukan":int(), "Pengeluaran":int(), "Sisa_uang":int(), "Tabungan":int()}
        data.append(list_bulan_baru)
    
def input_pemasukan(data, bulan): # Fungsi untuk input data pemasukan pada kolom pemasukan
    for row in data[1:]:  
        if row["Bulan"].capitalize() == bulan.capitalize():
            try:
                pemasukan = int(input(f"Masukkan pemasukan untuk {bulan}: "))
                row["Pemasukan"] = pemasukan
                print("Data Berhasil di Update!!")
                return
            
            except ValueError:
                print("Pemasukan harus berupa angka.\n")
                return
    print(f"Bulan '{bulan}' tidak ditemukan.\n")

def input_pengeluaran(data, bulan): # Fungsi untuk input data pengeluaran pada kolom pengeluaran
    for row in data[1:]:  
        if row["Bulan"].capitalize() == bulan.capitalize():
            try:
                pengeluaran = int(input(f"Masukkan pengeluaran untuk {bulan}: "))
                row["Pengeluaran"] = pengeluaran
                print("Data Berhasil di Update!!")
                return
            except ValueError:
                print("Pengeluaran harus berupa angka.\n")
                return
    print(f"Bulan '{bulan}' tidak ditemukan.\n")

def input_sisa_dan_tabungan(data, bulan): # Fungsi untuk menghitung Sisa uang dan tabungan
    bulan = bulan.capitalize()
    index_bulan = None

    # Temukan index dari bulan yang dimaksud
    for i in range(1, len(data)):
        if data[i]["Bulan"].capitalize() == bulan:
            index_bulan = i
            break

    if index_bulan is None:
        print(f"Bulan '{bulan}' tidak ditemukan.\n")
        return

    try:
        pemasukan = data[index_bulan]["Pemasukan"]
        pengeluaran = data[index_bulan]["Pengeluaran"]

        if not isinstance(pemasukan, int) or not isinstance(pengeluaran, int):
            print("Pemasukan dan Pengeluaran harus diisi terlebih dahulu.\n")
            return

        # Hitung sisa uang
        sisa_uang = pemasukan - pengeluaran
        data[index_bulan]["Sisa_uang"] = sisa_uang

        # Hitung tabungan akumulatif
        if index_bulan > 1:
            tabungan_sebelumnya = data[index_bulan - 1]["Tabungan"]
            if not isinstance(tabungan_sebelumnya, int):
                tabungan_sebelumnya = 0
        else:
            tabungan_sebelumnya = 0

        data[index_bulan]["Tabungan"] = tabungan_sebelumnya + sisa_uang
        print("Data Berhasil di Update")
    except Exception as e:
        print(f"Terjadi kesalahan saat menghitung: {e}")
    
def delete_kolom(data, nama_kolom): # Fungsi untuk menghapus Kolom
    # Cek apakah kolom ada di header
    if nama_kolom not in data[0]:
        print(f"Kolom '{nama_kolom}' tidak ditemukan.\n")
        return

    # Hapus kolom dari semua baris
    for row in data:
        if nama_kolom in row:
            del row[nama_kolom]

def membuat_kolom(): # Fungsi menu membuat kolom
        print("1. Tambah Kolom Baru")
        print("2. Selesai")
        while True:
            pilihan_buat = input("Masukan Pilihan Membuat Kolom Anda: ")
            if pilihan_buat == "1":
                tambah_key_baru = buatkey()
                if tambah_key_baru in data[0]:
                    print("Kolom Sudah Ada")
                    print("1. Tambah Kolom Baru")
                    print("2. Selesai")
                else: 
                    pilihan_save=input("Apakah Ingin Menyimpan Kolom Baru(y/n): ")
                    if pilihan_save == "y":
                        data[0][tambah_key_baru] = tambah_key_baru
                        lihatdata()
                        print("Kolom Berhasil Tersimpan")
                    elif pilihan_save == "n":
                        print("Kolom Tidak jadi Disimpan")
                    print("1. Tambah Kolom Baru")
                    print("2. Selesai")

            elif pilihan_buat == "2":
                    print ("=====Catatan Keuangan Pribadi=====")
                    print ("1. Membuat Kolom")
                    print ("2. Melihat Tabel")
                    print ("3. Mengupdate Tabel")
                    print ("4. Menghapus Tabel")
                    print ("5. Keluar")
                    return 
            else: 
                print("Pilihan tidak tersedia, tolong masukan kembali.\n")
                print("1. Tambah Kolom Baru")
                print("2. Selesai")

def melihat_tabel(): # Fungsi menu melihat tabel
    while True:
            print("1. Melihat data")
            print("2. Melihat kolom")
            print("3. Selesai")
            pilihan_read = input("Masukan Pilihan Melihat Tabel Anda: ")
            if pilihan_read == "1":
                tampilkan_data = input("Apakah Ingin Menampilkan Data (y/n): ")
                if tampilkan_data == "y":
                    lihatdata()

            elif pilihan_read == "2":
                tampilkan_data2 = input("Apakah Ingin Menampilkan Data? (y/n): ")
                if tampilkan_data2 == "y":
                    lihatkey()
                else:
                    print("Data Tidak Tersedia")
            elif pilihan_read == "3":
                print ("=====Catatan Keuangan Pribadi=====")
                print ("1. Membuat Kolom")
                print ("2. Melihat Tabel")
                print ("3. Mengupdate Tabel")
                print ("4. Menghapus Tabel")
                print ("5. Keluar")
                return 
            else:
                print("Pilihan tidak tersedia, tolong masukan kembali.\n")
                print("1. Melihat data")
                print("2. Melihat kolom")
                print("3. Selesai")

def mengupdate_tabel(): # Fungsi menu mengupdate tabel
    while True:
            print("1. Update Data")
            print("2. Selesai")
            pilihan_update = input("Masukan Pilihan Mengupdate Data: ")
            if pilihan_update == "1":
                lihatdata()
                masukan_key = masukankey()
                if masukan_key in data[0]:
                    pilihan_continue = input("Apakah Ingin Mengupdate Data?(y/n): ")
                    if pilihan_continue == "y":
                        if masukan_key == "Bulan":
                            input_bulan()
                            print("Data Berhasil di Update!!")

                        elif masukan_key == "Pemasukan":
                            pilih_bulan_pemasukan=input("Pilih Bulan Yang Ingin Di Update: ")
                            input_pemasukan(data,pilih_bulan_pemasukan)
                            

                        elif masukan_key == "Pengeluaran":
                            pilih_bulan_pengeluaran=input("Pilih Bulan Yang Ingin Di Update: ")
                            input_pengeluaran(data,pilih_bulan_pengeluaran)
                            
                            
                        elif masukan_key == "Sisa_uang":
                            pilih_bulan_sisa=input("Pilih Bulan Yang Ingin Di Update: ")
                            input_sisa_dan_tabungan(data, pilih_bulan_sisa)

                        else:
                            print("Data Tidak Tersedia")    
                    elif pilihan_continue =="n":
                        continue
                    else:
                        print("Salah Input Pilihan, Masukan Kembali Dengan Benar")
                else:
                    print("Data Tidak Tersedia")
            elif pilihan_update == "2":
                print ("=====Catatan Keuangan Pribadi=====")
                print ("1. Membuat Kolom")
                print ("2. Melihat Tabel")
                print ("3. Mengupdate Tabel")
                print ("4. Menghapus Tabel")
                print ("5. Keluar")
                return 
            else:
                print("Pilihan tidak tersedia, tolong masukan kembali.\n")
                print("1. Update Data")
                print("2. Selesai")

def menghapus_tabel(): #Fungsi menu menghapus tabel
    while True:
            print("1. Hapus Data")
            print("2. Selesai")
            pilihan_delete = input("Masukan Pilihan Menghapus Data: ")
            if pilihan_delete == "1":
                print("1. Hapus Kolom")
                print("2. Hapus Tabel")
                print("3. Kembali")
                pilihan_delete_key = input("Masukan Pilihan Menghapus: ")

                if pilihan_delete_key == "1":
                    masukan_key = masukankey()
                    if masukan_key in data[0]:
                        delete_kolom(data, masukan_key)
                        print("Kolom Berhasil dihapus")
                    else:
                        print("Kolom tidak ditemukan")

                elif pilihan_delete_key == "2":
                    data.clear()
                    print("Tabel Berhasil dihapus")

                elif pilihan_delete_key == "3":
                    continue

                else:
                    print("Pilihan tidak valid")

            elif pilihan_delete == "2":
                print ("=====Catatan Keuangan Pribadi=====")
                print ("1. Membuat Kolom")
                print ("2. Melihat Tabel")
                print ("3. Mengupdate Tabel")
                print ("4. Menghapus Tabel")
                print ("5. Keluar")
                return 
            else:
                print("Pilihan tidak tersedia, tolong masukan kembali.\n")
                

def main_menu(): #Fungsi menu utama
    print ("=====Catatan Keuangan Pribadi=====")
    print ("1. Membuat Kolom")
    print ("2. Melihat Tabel")
    print ("3. Mengupdate Tabel")
    print ("4. Menghapus Tabel")
    print ("5. Keluar")
    while True:
        pilihan_main = input("Masukan Pilihan Anda: ")
        if pilihan_main == "1":
            membuat_kolom()
        elif pilihan_main == "2":
            melihat_tabel()
        elif pilihan_main == "3":
            mengupdate_tabel()            
        elif pilihan_main =="4":
            menghapus_tabel()    
        elif pilihan_main =="5":
            break
        else:
            print("Input tidak valid, silahkan masukan kembali\n")
            print ("=====Catatan Keuangan Pribadi=====")
            print ("1. Membuat Kolom")
            print ("2. Melihat Tabel")
            print ("3. Mengupdate Tabel")
            print ("4. Menghapus Tabel")
            print ("5. Keluar")

main_menu()