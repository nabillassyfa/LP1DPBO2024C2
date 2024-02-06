/*

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

*/


class DPR{
    // variabel yang hanya dapat diakses dalam kelas itu saja
    private String id;
    private String nama;
    private String bidang;
    private String partai;
    char jenis_kelamin;

    // variabel yang dapat diakses oleh main
    public DPR(){

    }

    public DPR (String id, String nama, String bidang, String partai, char jk){
        // konstruction dengan inisialisasi
        this.id = id;
        this.nama = nama;
        this.bidang = bidang;
        this.partai = partai;
        this.jenis_kelamin = jk;
    }

    // Fungsi dan prosedur untuk get dan set ID
    public void setId (String id){
        this.id = id;
    }

    public String getId (){
        return this.id;
    }

    // Fungsi dan prosedur untuk get dan set Nama
    public void setnama (String nama){
        this.nama = nama;
    }

    public String getnama (){
        return this.nama;
    }

    // Fungsi dan prosedur untuk get dan set Nama Bidang
    public void setbidang (String bidang){
        this.bidang = bidang;
    }

    public String getbidang (){
        return this.bidang;
    }

    // Fungsi dan prosedur untuk get dan set Nama Partai
    public void setpartai (String partai){
        this.partai = partai;
    }

    public String getpartai (){
        return this.partai;
    }

    // Fungsi dan prosedur untuk get dan set Jenis Kelamin
    public void setJK (char jk){
        this.jenis_kelamin = jk;
    }

    public char getJK (){
        return this.jenis_kelamin;
    }

};