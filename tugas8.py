class SaldonipunMbotenCekapError(Exception):
    pass

class JumlahNegativeError(Exception):
    pass
        
class LepatPasswordError(Exception):
    pass
        
class LepatNoAccountError(Exception):
    pass

class BankJawi():
    def __init__(self, asmo, arto, password, no_akun):
        self.asmo = asmo
        self.arto = arto
        self.password = password
        self.no_akun = no_akun
        
    def periksa_akun(self, password, no_akun):
        if self.password != password:
            raise LepatPasswordError("Password e jenengan lepat")
        if self.no_akun != no_akun:
            raise LepatNoAccountError("No akun jenengan mboten wonten")
        
    def mendet_arto(self, jumlah, password, no_akun):
        self.periksa_akun(password, no_akun)
        if jumlah > self.arto:
            raise SaldonipunMbotenCekapError("arto jenengan mboten cekap")
        self.arto -= jumlah
        print(f"{self.asmo} mundhut {jumlah} rupiah. Saldonipun saiki {self.arto} rupiah.")
    
    def imbuh_arto(self, jumlah, password, no_akun):
        self.periksa_akun(password, no_akun)
        if jumlah < 0:
            raise JumlahNegativeError("Jumlah e mboten saged negatif")
        self.arto += jumlah
        print(f"{self.asmo} nambah {jumlah} rupiah. Saldonipun saiki {self.arto} rupiah.")
        
    def nimali_arto(self, password, no_akun):
        self.periksa_akun(password, no_akun)
        print(f"Saldonipun {self.asmo} saiki {self.arto} rupiah.")

    def transfer_arto(self, jumlah, password, no_akun):
        self.periksa_akun(password, no_akun)
        if jumlah < 0:
            raise JumlahNegativeError("Jumlah e mboten saged negatif")
        self.arto += jumlah
        print(f"{self.asmo} nambah {jumlah} rupiah. Saldonipun saiki {self.arto} rupiah.")
        
bankjowo = BankJawi("Joko", 1000000, "password123", "1234567890")

try:
    bankjowo.mendet_arto(500000, "password123", "1234567890")
    bankjowo.imbuh_arto(200000, "password123", "1234567890")
    bankjowo.nimali_arto("password123", "1234567890")
    bankjowo.transfer_arto(300000, "password123", "1234567890")
    bankjowo.mendet_arto(5000000, "password123", "1234567890")
except (SaldonipunMbotenCekapError, JumlahNegativeError, LepatPasswordError, LepatNoAccountError) as e:
    print(e)

except ValueError:

    print(
        "Input kedah awujud angka!"
    )

finally:

    print(
        "\nPamriksan transaksi sampun paripurna."
    )