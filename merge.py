import json
import os

def merge():
    dir_list = os.listdir('./dataLengkap')

    tmp = []
    #['Drop-Out/Putus Studi', 'Lulus', 'Non-Aktif', 'Aktif', 'Kampus Merdeka', 'Keluar', 'Cuti']
    status_allowed = [ 'Lulus', 'Non-Aktif', 'Aktif', 'Kampus Merdeka', 'Cuti']
    for dir in dir_list:
        with open(f'./dataLengkap/{dir}', 'r') as file:
            data = json.load(file)
            for i in data:
                status = i['dataLengkap']['datastatuskuliah'][-1]['nm_stat_mhs']
                
                if (status in status_allowed) :
                    tmp.append(i)

    with open('data.json', 'w+') as save:
        json.dump(tmp, save)