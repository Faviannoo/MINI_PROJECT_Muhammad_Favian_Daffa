data_mahasiswa = []

while True:
    print ("\n=== PENGELOLAAN NILAI MAHASISWA ===")
    print ("\n1. Tambah Nilai")
    print ("2. Tampilkan Nilai")
    print ("3. Ubah Nilai")
    print ("4. Hapus Nilai")
    print ("5. Keluar")
    pilihan = input("\nPilih Menu (1-5) :")

    
    if pilihan == "1":
        print("\n=== TAMBAHKAN DATA MAHASISWA ===")
        print()

        nama = input("Masukkan Nama Mahasiswa: ")

        while True:
            try:
                tugas = float(input("Masukkan Nilai Tugas (0-100) : "))

                if 0 <= tugas <= 100 :
                    break

                else :
                    print("Nilai Harus Antara 0-100")
            except ValueError:
                    print("Input Harus Berupa Angka")

        while True:
            try:
                uts = float(input("Masukkan Nilai UTS (0-100): "))
                if 0 <= uts <= 100:
                    break
                else:
                    print("Nilai Harus Antara 0-100")
            except ValueError:
                    print("Input Harus Berupa Angka")
    
        while True:
            try:
                uas = float(input("Masukkan Nilai UAS (0-100): "))

                if 0 <= uas <= 100:
                
                       break
                else:
                    print("Nilai Harus Antara 0-100")
            except ValueError:
                    print("Input Harus Berupa Angka")

        data_mahasiswa.append([nama, tugas, uts, uas])

        print ("Data Mahasiswa Berhasil Ditambahkan")

    elif pilihan == "2":
        print ("\n=== Data Nilai Mahasiswa ===")

        if len(data_mahasiswa) == 0:
            print("\nBelum Ada Data Mahasiswa")
        else :
             for i,data in enumerate(data_mahasiswa, start=1):
                nama = data[0]
                tugas = data[1]
                uts = data[2]
                uas = data[3]

                nilai_akhir = (tugas * 0.30) + (uts * 0.30) + (uas * 0.40)
                 
                if nilai_akhir >= 85:
                    grade = "A"
                elif nilai_akhir >= 75:
                    grade = "B"
                elif nilai_akhir >= 65:
                    grade = "C"
                elif nilai_akhir >= 50:
                    grade = "D"
                else:
                    grade = "E"

                print("\nData ke-",i)
                print("Nama        :", nama)
                print("Nilai Tugas :", tugas)
                print("Nilai UTS   :", uts)
                print("Nilai UAS   :", uas)   
                print("Grade       :", grade)

    elif pilihan == "3":
         print("\n=== UBAH DATA MAHASISWA ===")

         if len(data_mahasiswa) == 0:
              print("\nBelum Ada Data Mahasiswa")
         else :
            cari_nama = input("Masukkan Nama Mahasiswa Yang Ingin Diubah: ")

            for data in data_mahasiswa:
                if data[0] == cari_nama:
                    print("Data", data[0],"Ditemukan")
                    while True:
                        try:
                            tugas = float(input("Masukkan Nilai Tugas Baru (0-100): "))
                            if 0 <= tugas <= 100:
                                    break
                            else:
                                print("Nilai Harus Antara 0-100")
                        except ValueError:
                                print("Input Harus Berupa Angka")
                
                    while True:
                        try:
                            uts = float(input("Masukkan Nilai UTS Baru (0-100): "))
                            if 0 <= uts <= 100:
                                break
                            else:
                                print("Nilai Harus Antara 0-100")
                        except ValueError:
                                print("Input Harus Berupa Angka")
                
                    while True:
                        try:
                            uas = float(input("Masukkan Nilai UAS Baru (0-100): "))
                            if 0 <= uas <= 100:
                                break
                            else:
                                print("Nilai Harus Antara 0-100")
                        except ValueError:
                                print("Input Harus Berupa Angka")

                    data[1] = tugas
                    data[2] = uts
                    data[3] = uas

                    print("\nData Mahasiswa Berhasil Diubah")
                    break
            else:
                print("\nData mahasiswa tidak ditemukan")

    elif pilihan == "4":
        print("\n=== Hapus Data Mahasiswa ===")

        if len(data_mahasiswa) == 0:
            print("\nBelum Ada Data Mahasiswa")
        else :
            cari_nama = input("Masukkan Nama Mahasiswa Yang Ingin Dihapus: ")

            for data in data_mahasiswa:
                if data[0] == cari_nama:
                    data_mahasiswa.remove(data)
                    print("Data Mahasiswa ",data[0] ," Berhasil Dihapus")
                    break
            else :
                 print("\nData Mahasiswa Tidak Ditemukan")    

    elif pilihan == "5":
        print("\nTerima Kasih Telah Menggunakan Program")
        break

    else:
        print("\nPilihan Menu Tidak Tersedia!")
        print("Silakan Pilih Menu 1-5.")   