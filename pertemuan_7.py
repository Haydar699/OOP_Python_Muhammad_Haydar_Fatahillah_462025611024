class Minuman:
    def __init__(self,nama,harga):
        self.nama = nama
        self.harga = harga
    
    def info(self):
        print(f"Nama: {self.nama} \nHarga: {self.harga}")
    
    def ratting(self):
        print(f"Berikan Feedback dari {self.nama} tersebut!")
    
class Kopi(Minuman):
    def sajikan(self):
        print('Menyajikan kopi hangat ☕\n')
        
class Jus(Minuman):
    def sajikan(self):
        print('Menyajikan jus dingin 🧃\n')
        
class Teh(Minuman):
    def sajikan(self):
        print("Menyajikan teh manis 🍵\n")

def tampilkan_info(Minuman):
    Minuman.info()
    
def tampilkan_saji(Minuman):
    Minuman.sajikan()
    
kopi1 = Kopi("kopi hangat", 12000)
jus1 = Jus("jus mangga", 15000)
teh1 =Teh("teh manis", 10000)

print("*" * 7 + " Daftar Menu " + "*" * 7)
tampilkan_info(kopi1)
tampilkan_saji(kopi1)

tampilkan_info(jus1)
tampilkan_saji(jus1)

tampilkan_info(teh1)
tampilkan_saji(teh1)