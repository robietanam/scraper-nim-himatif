import requests


response = requests.get("https://pddikti.kemdikbud.go.id/search_mahasiswa/-/2124101020/B9507FAB-2874-4DCD-9C37-4C921C231210/FF6A1A63-7D32-48AF-BED1-38F71A2E1670")
with open("21", "w+") as file:
    file.write(response.content.decode())
    file.close()
