
# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin


from DPR import DPR

dewan = []
query = 0
# Program menjalankan query menambah, mengubah, dan hapus
while (query != 1):
    print () #mmenampilkan newline
    print ("=======================================")
    print ("*       Masukan jenis perintah :      *" )
    print ("=======================================")
    print ("1. Untuk menambah data anggota DPR " )
    print ("2. Untuk mengubah data anggota DPR " )
    print ("3. Untuk menghapus data anggota DPR" )
    print ("4. Untuk menampilkan data anggota DPR" )
    print ("5. Untuk mengakhiri program " )
    
    print () #mmenampilkan newline

    # masukan user untuk jenis query
    print ("Masukan perintah : ", end="")
    jenis = str (input())

    # Kondisi jika user ingin menambah data
    if (jenis == "1"):
        # memasukan jumlah data
        print ("Masukan jumlah data : " , end="")
        n = int (input())

        # memasukan data anggota DPR
        for i in range (n) :
            print () #mmenampilkan newline

            print ("ID :", end="")
            id = str (input ())
            print ("Nama :" , end="")
            nama = str (input ())
            print ("Nama bidang :" , end="")
            bidang = str (input ())
            print ("Nama partai :", end="" )
            partai = str (input ())
            print ("Jenis kelamin :" , end="")
            jk = input ()[0]

            dewan.append(DPR(id, nama, bidang, partai, jk))
    
    # Kondisi jika user ingin mengubah data
    elif (jenis == "2"):
        # Masukan untuk id data yang akan diubah
        print () #mmenampilkan newline
        print ("Masukan ID data yang akan diubah :" , end="")
        id_ubah = str (input ())

        # Masukan untuk data anggota DPR baru
        ketemu = 0
        indeks = 0
        
        while ketemu == 0 and indeks < len (dewan):
            anggota = dewan [indeks]
            if anggota.getId() == id_ubah : # kondisi id yang akan di ubah ada di dalam data
                # Menu data yang akan user ubah
                print ("!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!" )
                print ("!Pilih data yang ingin anda ubah !" )
                print ("!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!" )
                print ("  1. Nama Anggota" )
                print ("  2. Nama Bidang" )
                print ("  3. Nama Partai" )
                print ("  4. Jenis Kelamin" )
                print ("  5. Seluruhnya" )
                print () #mmenampilkan newline
                print ("Masukan perintah data yang ingin anda ubah:", end="")
                ubah = input ()[0]

                if (ubah == '1'):
                    print ("Nama Anggota:", end="" )
                    nama = str (input ())

                    anggota.setnama (nama)
                elif (ubah == '2'):
                    print ("Nama bidang :" , end="")
                    bidang = str (input ())

                    anggota.setbidang (bidang)
                elif (ubah == '3'):
                    print ("Nama partai :" , end="")
                    partai = str (input ())

                    anggota.setpartai (partai)
                elif (ubah == '4'):
                    print ("Jenis kelamin :" , end="")
                    jk = input ()[0]


                    anggota.setJK (jk)
                elif (ubah == '5'):
                    # Masukan user untuk data baru
                    print ("Nama :" , end="")
                    nama = str (input ())
                    print ("Nama bidang :" , end="")
                    bidang = str (input ())
                    print ("Nama partai :" , end="")
                    partai = str (input ())
                    print ("Jenis kelamin :" , end="")
                    jk = input ()[0]

                    # Program penggantian data anggota DPR
                    anggota.setnama (nama)
                    anggota.setbidang (bidang)
                    anggota.setpartai (partai)
                    anggota.setJK (jk)
                else:
                    print () #mmenampilkan newline
                    print ("!----------------------------!")
                    print (" Masukan perintah yang benar!" )
                    print ("!----------------------------!")
                

                ketemu = 1
            
            # iterasi
            indeks+=1
        

        # kondisi jika id tidak ada
        if (ketemu == 0):
            print ("!----------------------------!")
            print ("   Id Tidak ditemukan !")
            print ("!----------------------------!")
        

    elif (jenis == "3"):
        # Masukan user untuk id data yang akan dihapus
        print () #mmenampilkan newline
        print ("Masukan ID data yang akan dihapus :" , end="")
        id_hapus = str (input ())

        ketemu = 0
        indeks = 0
        
        while ketemu == 0 and indeks < len (dewan):
            anggota = dewan [indeks]
            if anggota.getId() == id_hapus : # kondisi id yang akan di ubah ada di dalam data
                dewan.remove(anggota)                      # menghapus data
                print () #mmenampilkan newline
                print ("Data berhasil dihapus !" )
                ketemu = 1
            
            # iterasi
            indeks+=1
        # kondisi jika id tidak ada
        if (ketemu == 0):
            print ("!----------------------------!")
            print ("    Id Tidak ditemukan !" )
            print ("!----------------------------!")
        
        
    # Kondisi jika user ingin mengakhiri query
    elif (jenis == "4"):
        # Menampilkan Output 
        if len(dewan) == 0:   # kondisi jika list kosong
            print ("Tidak ada Data yang tersimpan" )
        else:  # kondisi jika list tidak kosong
            print ("                      Data yang tersimpan               " )
            
            #program untuk mencari string terpanjang
            for perwakilan in dewan:
                panjang_id = max(10, len(str(perwakilan.getId())))
                panjang_nama = max(20, len(str(perwakilan.getnama())))
                panjang_bidang = max(11, len(str(perwakilan.getbidang())))
                panjang_partai = max(11, len(str(perwakilan.getpartai())))
                panjang_jk = max(13, len(str(perwakilan.getJK())))

            # mencetak garis tabel
            print ("!-{}-!-{}-!-{}-!-{}-!-{}-!".format('-' * panjang_id, '-' * panjang_nama, '-' * panjang_bidang, '-' * panjang_partai, '-' * panjang_jk))
            # header tabel
            print ("! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} !".format("ID" , panjang_id, "Nama" , panjang_nama, "Nama Bidang" , panjang_bidang, "Nama Partai" , panjang_partai, "Jenis Kelamin" , panjang_jk))
            # mencetak garis tabel
            print ("!-{}-!-{}-!-{}-!-{}-!-{}-!".format('-' * panjang_id, '-' * panjang_nama, '-' * panjang_bidang, '-' * panjang_partai, '-' * panjang_jk))
            
           
            # menampilkan data anggota dpr
            for perwakilan in dewan:
                print ("! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} ! {:<{}} !".format(perwakilan.getId() , panjang_id, perwakilan.getnama() , panjang_nama, perwakilan.getbidang(), panjang_bidang, perwakilan.getpartai() , panjang_partai, perwakilan.getJK() , panjang_jk))
               
            
            # mencetak garis tabel
            print ("!-{}-!-{}-!-{}-!-{}-!-{}-!".format('-' * panjang_id, '-' * panjang_nama, '-' * panjang_bidang, '-' * panjang_partai, '-' * panjang_jk))
        

    elif (jenis == "5"):
        query = 1

    # Kondisi jika query yang diinginkan tidak ada dalam daftar
    else :
        print ("query tidak ditemukan, masukan query yang sah" )
    

 