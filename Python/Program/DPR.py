
# Saya Nabilla Assyfa Ramadhani [2205297] 
# mengerjakan Latihan
# dalam mata Desain dan Pemograman Berorientasi Objek 
# untuk keberkahanNya maka saya tidak melakukan kecurangan 
# seperti yang telah dispesifikasikan. 
# Aamiin


class DPR :
    # variabel yang hanya dapat diakses dalam kelas itu saja
    __id = ""
    __nama = ""
    __bidang = ""
    __partai = ""
    __jenis_kelamin =' '

#variabel yang dapat diakses oleh main
# Construction untuk new pada class
    def __init__(self, id = "", nama = "", bidang = "", partai = "", jk = ''):
        #konstruction dengan inisialisasi
        self.__id = id
        self.__nama = nama
        self.__bidang = bidang
        self.__partai = partai
        self.__jenis_kelamin = jk
    
    
    #Metode set untuk id
    def setId (self, id):
        self.__id = id
    
    #Metode get untuk id
    def getId (self):
        return self.__id
    

    #Metode set untuk nama
    def setnama (self, nama):
        self.__nama = nama
    
    #Metode get untuk nama
    def getnama (self):
        return self.__nama
    

    #Metode set untuk nama bidang
    def setbidang (self, bidang):
        self.__bidang = bidang
    
    #Metode get untuk nama bidang
    def getbidang (self):
        return self.__bidang
    

    #Metode set untuk nama partai
    def setpartai (self, partai):
        self.__partai = partai
    
    #Metode get untuk nama partai
    def getpartai (self):
        return self.__partai
    

    #Metode set untuk jenis kelamin
    def setJK (self, jk):
        self.__jenis_kelamin = jk
    
    #Metode get untuk jenis kelamin
    def getJK (self):
        return self.__jenis_kelamin
    

