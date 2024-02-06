
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
    print ("=======================================")
    print ("*       Masukan jenis perintah :      *" )
    print ("=======================================")
    print ("1. Untuk menambah data anggota DPR " )
    print ("2. Untuk mengubah data anggota DPR " )
    print ("3. Untuk menghapus data anggota DPR" )
    print ("4. Untuk menampilkan data anggota DPR" )
    print ("5. Untuk mengakhiri program " )

    # masukan user untuk jenis query
    jenis = str (input())

    # Kondisi jika user ingin menambah data
    if (jenis == "1"):
        # memasukan jumlah data
        print ("Masukan jumlah data : " )
        n = int (input())

        # memasukan data anggota DPR
        for i in range (n) :

            print ("ID :")
            id = str (input ())
            print ("nama :" )
            nama = str (input ())
            print ("bidang :" )
            bidang = str (input ())
            print ("partai :" )
            partai = str (input ())
            print ("jenis kelamin :" )
            jk = input ()[0]

            dewan.append(DPR(id, nama, bidang, partai, jk))
    
    # Kondisi jika user ingin mengubah data
    elif (jenis == "2"):
        # Masukan untuk id data yang akan diubah
        print ("masukan id data yang akan diubah" )
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

                ubah = input ()[0]

                if (ubah == '1'):
                    print ("Nama Anggota:" )
                    nama = str (input ())

                    anggota.setnama (nama)
                elif (ubah == '2'):
                    print ("Nama bidang :" )
                    bidang = str (input ())

                    anggota.setbidang (bidang)
                elif (ubah == '3'):
                    print ("Nama partai :" )
                    partai = str (input ())

                    anggota.setpartai (partai)
                elif (ubah == '4'):
                    print ("jenis kelamin :" )
                    jk = input ()[0]


                    anggota.setJK (jk)
                elif (ubah == '5'):
                    # Masukan user untuk data baru
                    print ("nama :" )
                    nama = str (input ())
                    print ("bidang :" )
                    bidang = str (input ())
                    print ("partai :" )
                    partai = str (input ())
                    print ("jenis kelamin :" )
                    jk = input ()[0]

                    # Program penggantian data anggota DPR
                    anggota.setnama (nama)
                    anggota.setbidang (bidang)
                    anggota.setpartai (partai)
                    anggota.setJK (jk)
                else:
                    print ("Data yang akan diubah tidak ada" )
                

                ketemu = 1
            
            # iterasi
            indeks+=1
        

        # kondisi jika id tidak ada
        if (ketemu == 0):
            print ("Id Tidak ditemukan !")
        

    elif (jenis == "3"):
        # Masukan user untuk id data yang akan dihapus
        print ("masukan id data yang akan dihapus" )
        id_hapus = str (input ())

        ketemu = 0
        indeks = 0
        
        while ketemu == 0 and indeks < len (dewan):
            anggota = dewan [indeks]
            if anggota.getId() == id_hapus : # kondisi id yang akan di ubah ada di dalam data
                dewan.remove(anggota)                      # menghapus data
                print ("Data Terhapus !" )
                ketemu = 1
            
            # iterasi
            indeks+=1
        # kondisi jika id tidak ada
        if (ketemu == 0):
            print ("Id Tidak ditemukan !" )
        
        
    # Kondisi jika user ingin mengakhiri query
    elif (jenis == "4"):
        # Menampilkan Output 
        if len(dewan) == 0:   # kondisi jika list kosong
            print ("Tidak ada Data yang tersimpan    " )
        else:  # kondisi jika list tidak kosong
            print ("                                Data yang tersimpan               " )
            print ("!---------------------------------------------------------------------------------!" )
            print ("!  No  !   Id    !   Nama      !     Nama Bidang     ! Nama Partai! Jenis Kelamin !" )
            print ("!---------------------------------------------------------------------------------!" )
        
            i = 0 
            for perwakilan in dewan:
                print ("|" , str(i + 1), "." , " | ", perwakilan.getId() , "  |  " , perwakilan.getnama() , "   |    " , perwakilan.getbidang() , "      |    " , perwakilan.getpartai() ,  "   | " , perwakilan.getJK() ,"           |" )
                i+=1
            
            print ("!---------------------------------------------------------------------------------!" )
        

    elif (jenis == "5"):
        query = 1

    # Kondisi jika query yang diinginkan tidak ada dalam daftar
    else :
        print ("query tidak ditemukan, masukan query yang sah" )
    

 