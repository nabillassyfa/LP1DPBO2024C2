<!-- 

Saya Nabilla Assyfa Ramadhani [2205297] 
mengerjakan Latihan 1
dalam mata Desain dan Pemograman Berorientasi Objek 
untuk keberkahanNya maka saya tidak melakukan kecurangan 
seperti yang telah dispesifikasikan. 
Aamiin
 -->


<?php

// memanggil objek dpr
require ('DPR.php');
// memanggil link style.css
echo '<link rel="stylesheet" href="Pictures/style.css">';
// deklarasi list
$list = [];

// PROGRAM MEMASUKAN DATA
// membuat data baru
$anggota1 = new DPR ('123', 'Do Kyung Soo', 'Teknologi', 'PKS', 'L', 'Pictures/do.jpeg');
$anggota2 = new DPR ('125', 'Jay', 'Luar Negri', 'PAN', 'L', 'Pictures/2.jpg');

// memasukan data kedalam list
array_push($list, $anggota1);
array_push($list, $anggota2);

// menampilkan data
echo "<h2 style='text-align: center;'>Berikut Anggota DPR aktif</h2>";
echo '<table id="dpr">';
    // header tabel
    echo "<tr>";
    echo "<th>ID</th>";
    echo "<th>Foto Profil</th>";
    echo "<th>Nama</th>";
    echo " <th>Nama Bidang</th>";
    echo "<th>Nama Partai</th>";
    echo "<th>Jenis Kelamin</th>";
    echo " </tr>";

    // menampilkan data didalam list
    foreach ($list as $anggota) {
        echo "<tr>";
        echo "<td>" . $anggota->getId() . "</td>";
        echo "<td><img src='" . $anggota->getFotoProfil() . "' width='100px' height='150px'></td>";
        echo "<td>" . $anggota->getNama() . "</td>";
        echo "<td>" . $anggota->getBidang() . "</td>";
        echo "<td>" . $anggota->getPartai() . "</td>";
        echo "<td>" . $anggota->getJenisKelamin() . "</td>";
        echo "</tr>";
    }
    
echo "</table>";

// PROGRAM UPDATE DATA
$id_ubah = "123";     // id yang akan di update

// mengubah data anggota
foreach ($list as $anggota) {
    if ($anggota->getId () == $id_ubah){
        $anggota->setnama('Na Jaemin');
        $anggota->setBidang('Kesehatan');
        $anggota->setPartai('NCT');
        $anggota->setFotoProfil('Pictures/nana.jpg');
    }
}

// menampilkan data
echo "<h3 style='text-align: center;'><strong><em>Anggota dengan Id $id_ubah berhasil di Update!</em></strong></h3>";
echo "<h2 style='text-align: center;'>Berikut Anggota DPR aktif</h2>";
echo '<table id="dpr">';
    // header tabel
    echo "<tr>";
    echo "<th>ID</th>";
    echo "<th>Foto Profil</th>";
    echo "<th>Nama</th>";
    echo " <th>Nama Bidang</th>";
    echo "<th>Nama Partai</th>";
    echo "<th>Jenis Kelamin</th>";
    echo " </tr>";

    // menampilkan data didalam list
    foreach ($list as $anggota) {
        echo "<tr>";
        echo "<td>" . $anggota->getId() . "</td>";
        echo "<td><img src='" . $anggota->getFotoProfil() . "' width='100px' height='150px'></td>";
        echo "<td>" . $anggota->getNama() . "</td>";
        echo "<td>" . $anggota->getBidang() . "</td>";
        echo "<td>" . $anggota->getPartai() . "</td>";
        echo "<td>" . $anggota->getJenisKelamin() . "</td>";
        echo "</tr>";
    }
    
echo "</table>";

// PROGRAM MENGHAPUS DATA
$id_hapus = "125";   // id yang akan dihapus

// menghapus data
foreach ($list as $key => $anggota) {
    if ($anggota->getId() == $id_hapus) {
        unset($list[$key]); 
    }
}

echo "<h3 style='text-align: center;'><strong><em>Anggota dengan Id $id_hapus berhasil di hapus!</em></strong></h3>";
// menampilkan data
echo "<h2 style='text-align: center;'>Berikut Anggota DPR aktif</h2>";
echo '<table id="dpr">';
    // header tabel
    echo "<tr>";
    echo "<th>ID</th>";
    echo "<th>Foto Profil</th>";
    echo "<th>Nama</th>";
    echo " <th>Nama Bidang</th>";
    echo "<th>Nama Partai</th>";
    echo "<th>Jenis Kelamin</th>";
    echo " </tr>";

    // menampilkan data didalam list
    foreach ($list as $anggota) {
        echo "<tr>";
        echo "<td>" . $anggota->getId() . "</td>";
        echo "<td><img src='" . $anggota->getFotoProfil() . "' width='100px' height='150px'></td>";
        echo "<td>" . $anggota->getNama() . "</td>";
        echo "<td>" . $anggota->getBidang() . "</td>";
        echo "<td>" . $anggota->getPartai() . "</td>";
        echo "<td>" . $anggota->getJenisKelamin() . "</td>";
        echo "</tr>";
    }
    
echo "</table>";
?>