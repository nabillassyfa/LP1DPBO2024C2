<!-- 

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan 1
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin

 -->

<?php

class DPR{
    private $id = '';
    private $nama ='';
    private $bidang = '';
    private $partai = '';
    private $jenis_kelamin = '';
    private $foto_profil = ''; 

    public function __construct ($id ='', $nama='', $bidang='', $partai='', $jk='', $foto_profil=''){
        $this->id = $id;
        $this->nama = $nama;
        $this->bidang = $bidang;
        $this->partai = $partai;
        $this->jenis_kelamin = $jk;
        $this->foto_profil = $foto_profil; 
    }

    // Metode set untuk atribut foto profil
    public function setFotoProfil($foto_profil){
        $this->foto_profil = $foto_profil;
    }

    // Metode get untuk atribut foto profil
    public function getFotoProfil(){
        return $this->foto_profil;
    }

    // Metode set dan get untuk id
    public function setId($id){
        $this->id = $id;
    }

    public function getId(){
        return $this->id;
    }

    // Metode set dan get untuk nama
    public function setNama($nama){
        $this->nama = $nama;
    }

    public function getNama(){
        return $this->nama;
    }

    // Metode set dan get untuk bidang
    public function setBidang($bidang){
        $this->bidang = $bidang;
    }

    public function getBidang(){
        return $this->bidang;
    }

    // Metode set dan get untuk partai
    public function setPartai($partai){
        $this->partai = $partai;
    }

    public function getPartai(){
        return $this->partai;
    }

    // Metode set dan get untuk jenis kelamin
    public function setJenisKelamin($jk){
        $this->jenis_kelamin = $jk;
    }

    public function getJenisKelamin(){
        return $this->jenis_kelamin;
    }  

}

?>
