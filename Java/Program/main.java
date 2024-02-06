/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/

import java.util.Scanner;
import java.util.ArrayList;
import java.util.Iterator;

public class main {
    public static void main (String [] args){

    int i, n= 0, query = 0;
    String id, nama, bidang, partai;
    char jk;

    String jenis; // untuk menampung masukan menambah, mengubah, dan menghapus
    
    ArrayList <DPR> list = new ArrayList <>();

    Scanner sc = new Scanner (System.in);

    // Program menjalankan query menambah, mengubah, dan hapus
    while (query != 1){
        System.out.println( "=======================================");
        System.out.println( "*       Masukan jenis perintah :      *" );
        System.out.println( "=======================================");
        System.out.println( "1. Untuk menambah data anggota DPR " );
        System.out.println( "2. Untuk mengubah data anggota DPR " );
        System.out.println( "3. Untuk menghapus data anggota DPR" );
        System.out.println( "4. Untuk menampilkan data anggota DPR");
        System.out.println( "5. Untuk mengakhiri program " );

        // masukan user untuk jenis query
        jenis = sc.next();

        // Kondisi jika user ingin menambah data
        if (jenis.equals ("1")){
            // memasukan jumlah data
            System.out.println( "Masukan jumlah data : " );
            n = sc.nextInt();

            // memasukan data anggota DPR
            for (i = 0; i < n; i++){
                DPR temp = new DPR ();

                System.out.println( "ID :" );
                id = sc.next();
                System.out.println( "nama :" );
                nama = sc.next();
                System.out.println( "bidang :" );
                bidang = sc.next();
                System.out.println( "partai :" );
                partai = sc.next();
                System.out.println( "jenis kelamin :" );
                jk = sc.next().charAt (0);

                // Memasukan data ke dalam list
                temp.setId (id);
                temp.setnama (nama);
                temp.setbidang (bidang);
                temp.setpartai (partai);
                temp.setJK (jk);

                list.add (temp);
            }
        
        // Kondisi jika user ingin mengubah data
        }else if (jenis.equals ("2")){
            // Masukan untuk id data yang akan diubah
            String id_ubah;
            System.out.println( "masukan id data yang akan diubah" );
            id_ubah = sc.next();

            // Masukan untuk data anggota DPR baru
            int ketemu = 0;
            Iterator <DPR> it = list.iterator();
            while (ketemu == 0 && it.hasNext()){            // pengulangan selama id belum ditemukan
                DPR dewan = it.next();
                if (dewan.getId ().equals (id_ubah)){                     // kondisi id yang akan di ubah ada di dalam data
                    
                    System.out.println( "!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!" );
                    System.out.println( "!Pilih data yang ingin anda ubah !" );
                    System.out.println( "!~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~!" );
                    System.out.println( "  1. Nama Anggota" );
                    System.out.println( "  2. Nama Bidang" );
                    System.out.println( "  3. Nama Partai" );
                    System.out.println( "  4. Jenis Kelamin" );
                    System.out.println( "  5. Seluruhnya" );

                    char ubah;
                    ubah = sc.next().charAt (0);

                    if (ubah == '1'){
                        System.out.println( "Nama Anggota:" );
                        nama = sc.next();

                        dewan.setnama (nama);
                    }else if (ubah == '2'){
                        System.out.println( "Nama bidang :" );
                        bidang = sc.next();

                        dewan.setbidang (bidang);
                    }else if (ubah == '3'){
                        System.out.println( "Nama partai :" );
                        partai = sc.next();

                        dewan.setpartai (partai);
                    }else if (ubah == '4'){
                        System.out.println( "jenis kelamin :" );
                        jk = sc.next().charAt(0);

                        dewan.setJK (jk);
                    }else if (ubah == '5'){
                        // Masukan user untuk data baru
                        System.out.println( "nama :" );
                        nama = sc.next();
                        System.out.println( "bidang :" );
                        bidang = sc.next();
                        System.out.println( "partai :" );
                        partai = sc.next();
                        System.out.println( "jenis kelamin :" );
                        jk = sc.next().charAt(0);

                        // Program penggantian data anggota DPR
                        dewan.setnama (nama);
                        dewan.setbidang (bidang);
                        dewan.setpartai (partai);
                        dewan.setJK (jk);
                    }else{
                        System.out.println( "Data yang akan diubah tidak ada" );
                    }

                    ketemu = 1;
                }
            }
            if (ketemu == 0){
                System.out.println( "Id Tidak ditemukan !" );
            }

        }else if (jenis.equals ("3")){
            // Masukan user untuk id data yang akan dihapus
            System.out.println( "masukan id data yang akan dihapus" );
            String id_hapus;
            id_hapus = sc.next();

            int ketemu = 0;
            Iterator <DPR> it = list.iterator();
            while (ketemu == 0 && it.hasNext()){            // pengulangan selama id belum ditemukan
                DPR dewan = it.next();  
                if (dewan.getId ().equals (id_hapus)){             // kondisi jika id ditemukan
                    list.remove (dewan);                      // menghapus data
                    ketemu = 1;
                }
            }

            if (ketemu == 0){
                System.out.println( "Id Tidak ditemukan !" );
            }
        
      }else if (jenis.equals ("4")){
            // Menampilkan Output 
            if (list.isEmpty ()){   // kondisi jika list kosong
                System.out.println("Tidak ada Data yang tersimpan    " );
            }else{  // kondisi jika list tidak kosong
                System.out.println("                                Data yang tersimpan               ");
                System.out.println("!---------------------------------------------------------------------------------!" );
                System.out.println("!  No  !   Id    !   Nama      !     Nama Bidang     ! Nama Partai! Jenis Kelamin !" );
                System.out.println("!---------------------------------------------------------------------------------!" );
            
                for (i = 0; i < list.size(); i++){
                    System.out.println("|  " + (i + 1) + "." + "  |   "+ list.get(i).getId() + "  |   " + list.get(i).getnama() + "    |    " + list.get(i).getbidang() + "        |    " + list.get(i).getpartai() +  "      | " + list.get(i).getJK() + "            |" );
                }
               System.out.println("!---------------------------------------------------------------------------------!" );
            }

        }else if (jenis.equals ("5")){
            query = 1;

        // Kondisi jika query yang diinginkan tidak ada dalam daftar
        }else {
            System.out.println("query tidak ditemukan, masukan query yang sah" );
        }

        
    }
    sc.close ();
    }
}