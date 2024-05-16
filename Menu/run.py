import subprocess

arquivos = ["Menu/config.py","Menu/Menus.py","Menu/jogo.py"]

for arquivo in arquivos:
    subprocess.run(['python', arquivo])
    