class Mahasiswa:
    prodi = ""
    asal = ""
    
    def salam(self,nama):
        print(f"Assalamualaikum, perkenalkan namaku {nama}, aku berasal dari {self.asal}")
    def belajar(self,kampus):
        print(f"Di {kampus} ini, aku mengambil jurusan {self.prodi}")
    @staticmethod
    def tinggal(asrama):
        print(f"saat ini aku tinggal di asrama {asrama}")

# object 1
seno = Mahasiswa()
seno.prodi = "TI"
seno.asal = "solo"
seno.salam("seno")
seno.belajar("unida")
seno.tinggal("umar\n")

# object 2
joko = Mahasiswa()
joko.prodi = "TIP"
joko.asal = "kendal"
joko.salam("joko")
joko.belajar("unida")
joko.tinggal("usman")
    
