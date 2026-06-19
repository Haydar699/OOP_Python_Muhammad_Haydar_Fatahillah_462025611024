class President:
    def __init__(self,nama,tahun,julukan):
        self.nama = nama
        self.tahun = tahun
        self.julukan = julukan
pres1 = President("Sorekarno","1945-19567","Proklamator")
pres2 = President("soeharto","1966-1998","Bpk. Pembangunan")
pres3 = President("Habibie","1998-1999","Bpk. Teknologi")

print(f"President ke-1 = {pres1.nama}, {pres1.tahun}, {pres1.julukan}")
print(f"President ke-2 = {pres2.nama}, {pres2.tahun}, {pres2.julukan}")
print(f"President ke-3 = {pres3.nama}, {pres3.tahun}, {pres3.julukan}")
