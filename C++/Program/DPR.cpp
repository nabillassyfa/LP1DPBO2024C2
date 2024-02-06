/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/

#include <iostream>
#include <string>

using namespace std;

class DPR{
    private:  // variabel yang hanya dapat diakses dalam kelas itu saja
        string id;
        string nama;
        string bidang;
        string partai;
        char jenis_kelamin;

    public:  // variabel yang dapat diakses oleh main
        // Construction untuk new pada class
        DPR(){

        }

        DPR (string id, string nama, string bidang, string partai, char jk){
            // konstruction dengan inisialisasi
            this->id = id;
            this->nama = nama;
            this->bidang = bidang;
            this->partai = partai;
            this->jenis_kelamin = jk;
        }

        //Metode set untuk id
        void setId (string id){
            this->id = id;
        }
        //Metode get untuk id
        string getId (){
            return this->id;
        }

        //Metode set untuk nama
        void setnama (string nama){
            this->nama = nama;
        }
        //Metode get untuk nama
        string getnama (){
            return this->nama;
        }

        //Metode set untuk nama bidang
        void setbidang (string bidang){
            this->bidang = bidang;
        }
        //Metode get untuk nama bidang
        string getbidang (){
            return this->bidang;
        }

        //Metode set untuk nama partai
        void setpartai (string partai){
            this->partai = partai;
        }
        //Metode get untuk nama partai
        string getpartai (){
            return this->partai;
        }

        //Metode set untuk jenis kelamin
        void setJK (char jk){
            this->jenis_kelamin = jk;
        }
        //Metode get untuk jenis kelamin
        char getJK (){
            return this->jenis_kelamin;
        }
        
        // Destruction
        ~DPR(){

        }

};