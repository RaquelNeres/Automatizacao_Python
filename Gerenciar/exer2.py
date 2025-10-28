import shutil
from pathlib import Path

pasta = Path("imagens")
arquivo1 = Path("imagens/tete.png")
arquivo2 = Path("imagens/popo.png")
pasta.mkdir()
arquivo1.touch()
arquivo2.touch()

shutil.copytree("imagens", "backup")

# two
ar = Path("relatorio.txt")
if ar.exists():
    shutil.copy2("relatorio.txt", "relatorios_antigos/relatorio_backup.txt")


# 3
novo = Path("extraido")
novo.mkdir()

shutil.unpack_archive("arquivos_secretos.zip", "extraido")

for a in novo.iterdir():
    print(a.name)