from pprint import pprint as p
from pddiktipy.api import api
from pddiktipy.helper import helper
import json

from merge import merge


h = helper()
a = api()
angkatan = ['17', '18', '19', '20', '21', "22", '23', '24'] 

def getData():
    for i in angkatan: 
        dataMhs = a.specific_search_mhs(nipd=f"{i}241010", pt="Universitas Jember", prodi="Teknologi Informasi")
        with open(f"dump/{i}", "w+") as file:
            json.dump(dataMhs, file)
            
            print(f"{i} Done")

def getDataLengkap():
    for i in angkatan:
        dataMahasiswaLengkap = []
        with open(f"dump/{i}", "rb") as file:
                data = json.load(file)
                dataMhs = data['mahasiswa']
                for mhs in dataMhs:
                    dataMhs = a.detail_mahasiswa_by_weblink(mhs['id'])
                    dataMahasiswaLengkap.append({"mahasiswa" : mhs, "dataLengkap" : dataMhs})
                    
                    print(mhs['nama'] + " DONE")
        with open(f"dataLengkap/{i}", "w+") as file:
            json.dump(dataMahasiswaLengkap, file)
        print("Angkatan " + i + " DONE")


if __name__ == "__main__":
    getData()
    getDataLengkap()
    merge()