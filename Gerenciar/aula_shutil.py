import shutil
from pathlib import Path

# pode renomear

# salva meta dados de criação 
shutil.copy2("arquivinho.txt", "backup/arquivinho_backup.txt") # copiar arquivo
# a pasta de destino nao precisa existir
shutil.copytree("meus_arquivos", "meus_arquivos_backup", dirs_exist_ok=True) # copiar pasta com arquivos para outra

shutil.move("meus_arquivos/arquivo_teste.txt", "meus_arquivos/arquivo.txt")

shutil.rmtree("meus_arquivos_backup") # deletar pasta

shutil.make_archive("meus_arquivos", "zip", "meus_arquivos") # zipar e renomar

shutil.unpack_archive("meus_arquivos.zip", "arquivos") # extrair zip 

arquivos = Path("arquivos")
arquivos_backup = Path("arquivos_backup")

shutil.copytree(arquivos, arquivos_backup) #