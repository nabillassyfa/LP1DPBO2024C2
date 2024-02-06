/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/

// deklarasi library
#include <bits/stdc++.h>  // include semua library di cpp
#include "DPR.cpp"


using namespace std;

int main (){
    int i, n= 0, query = 0;   // variabel untuk iterasi, menampung banyak data, dan pengulangan query
    string id, nama, bidang, partai;
    char jk;

    string jenis; // untuk menampung masukan menambah, mengubah, dan menghapus
    
    list <DPR> llist;

    // Program menjalankan query menambah, mengubah, dan hapus
    while (query != 1){
        cout << "======================================="<< endl;
        cout << "*       Masukan jenis perintah :      *" << endl;
        cout << "======================================="<< endl;
        cout << "1. Untuk menambah data anggota DPR " << endl;
        cout << "2. Untuk mengubah data anggota DPR " << endl;
        cout << "3. Untuk menghapus data anggota DPR" << endl;
        cout << "4. Untuk menampilkan data anggota DPR" << endl;
        cout << "5. Untuk mengakhiri program " << endl;

        // masukan user untuk jenis query
        cin >> jenis;

        // Kondisi jika user ingin menambah data
        if (jenis == "1"){
            // memasukan jumlah data
            cout << "Masukan jumlah data : " << endl;
            cin >> n;

            // memasukan data anggota DPR
            for (i = 0; i < n; i++){
                DPR temp;

                cout << "ID :" << endl;
                cin >> id;
                cout << "nama :" << endl;
                cin >> nama;
                cout << "bidang :" << endl;
                cin >> bidang;
                cout << "partai :" << endl;
                cin >> partai;
                cout << "jenis kelamin :" << endl;
                cin >> jk;

                // Memasukan data ke dalam list
                temp.setId (id);
                temp.setnama (nama);
                temp.setbidang (bidang);
                temp.setpartai (partai);
                temp.setJK (jk);

                llist.push_back (temp);
            }
        
        // Kondisi jika user ingin mengubah data
        }else if (jenis == "2"){
            // Masukan untuk id data yang akan diubah
            string id_ubah;
            cout << "masukan id data yang akan diubah" << endl;
            cin >> id_ubah;

            char ubah;
            // Masukan untuk data anggota DPR baru
            int ketemu = 0;
            list <DPR> :: iterator it = llist.begin ();
            while (ketemu == 0 && it != llist.end ()){            // pengulangan selama id belum ditemukan
                if (it->getId () == id_ubah){                     // kondisi id yang akan di ubah ada di dalam data

                    // Menu data yang akan user ubah
                    cout << "!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!" << endl;
                    cout << "!Pilih data yang ingin anda ubah !" << endl;
                    cout << "!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!" << endl;
                    cout << "  1. Nama Anggota" << endl;
                    cout << "  2. Nama Bidang" << endl;
                    cout << "  3. Nama Partai" << endl;
                    cout << "  4. Jenis Kelamin" << endl;
                    cout << "  5. Seluruhnya" << endl;

                    cin >> ubah;

                    if (ubah == '1'){
                        cout << "Nama Anggota:" << endl;
                        cin >> nama;

                        it->setnama (nama);
                    }else if (ubah == '2'){
                        cout << "Nama bidang :" << endl;
                        cin >> bidang;

                        it->setbidang (bidang);
                    }else if (ubah == '3'){
                        cout << "Nama partai :" << endl;
                        cin >> partai;

                        it->setpartai (partai);
                    }else if (ubah == '4'){
                        cout << "jenis kelamin :" << endl;
                        cin >> jk;

                        it->setJK (jk);
                    }else if (ubah == '5'){
                        // Masukan user untuk data baru
                        cout << "nama :" << endl;
                        cin >> nama;
                        cout << "bidang :" << endl;
                        cin >> bidang;
                        cout << "partai :" << endl;
                        cin >> partai;
                        cout << "jenis kelamin :" << endl;
                        cin >> jk;

                        // Program penggantian data anggota DPR
                        it->setnama (nama);
                        it->setbidang (bidang);
                        it->setpartai (partai);
                        it->setJK (jk);
                    }else{
                        cout << "Data yang akan diubah tidak ada" << endl;
                    }

                    ketemu = 1;
                }
                // iterasi
                it++;
            }

            // kondisi jika id tidak ada
            if (ketemu == 0){
                cout << "Id Tidak ditemukan !" << endl;
            }

        }else if (jenis == "3"){
            // Masukan user untuk id data yang akan dihapus
            cout << "masukan id data yang akan dihapus" << endl;
            string id_hapus;
            cin >> id_hapus;

            int ketemu = 0;
            list <DPR> :: iterator it = llist.begin ();
            while (ketemu == 0 && it != llist.end ()){     // pengulangan selama id belum ditemukan
                if (it->getId () == id_hapus){             // kondisi jika id ditemukan
                    llist.erase (it);                      // menghapus data
                    cout << "Data Terhapus !" << endl;
                    ketemu = 1;
                }
                // iterasi
                it++;
            }

            // kondisi jika id tidak ada
            if (ketemu == 0){
                cout << "Id Tidak ditemukan !" << endl;
            }
         
        // Kondisi jika user ingin mengakhiri query
        }else if (jenis == "4"){
            // Menampilkan Output 
            if (llist.empty ()){   // kondisi jika list kosong
                cout << "Tidak ada Data yang tersimpan    " << endl;
            }else{  // kondisi jika list tidak kosong
                cout << "                                Data yang tersimpan               " << "\n\n";
                cout << "!---------------------------------------------------------------------------------!" << endl;
                cout << "!  No  !   Id    !   Nama      !     Nama Bidang     ! Nama Partai! Jenis Kelamin !" << endl;
                cout << "!---------------------------------------------------------------------------------!" << endl;
            
                i = 0; 
                for (list <DPR> :: iterator it = llist.begin (); it != llist.end(); it++){
                    cout << "|  " << (i + 1) << "." << "  |   "<< it->getId() << "  |   " << it->getnama() << "    |    " << it->getbidang() << "        |    " << it->getpartai() <<  "      | " << it->getJK() << "            |" << endl;
                    i++;
                }
               cout << "!---------------------------------------------------------------------------------!" << endl;
            }

        }else if (jenis == "5"){
            query = 1;

        // Kondisi jika query yang diinginkan tidak ada dalam daftar
        }else {
            cout << "query tidak ditemukan, masukan query yang sah" << endl;
        }

        // newline :)
        cout << "" << endl;
    }

    
   
   
   

    return 0;
}