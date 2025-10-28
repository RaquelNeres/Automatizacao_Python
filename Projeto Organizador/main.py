# Projeto: Organizador de Arquivos por Extensão
from pathlib import Path
import shutil
from datetime import datetime

registro = Path("Projeto Organizador/registro.log")

def organizar(pasta):
    ex = []
    t_arquivo = 0

    for arquivo in pasta.iterdir(): # busca por tudo sem filtro
        if not arquivo.is_file():
            continue  # pular se nao for arquivo

        extensao  = arquivo.suffix
        pasta_ex = Path(f"Projeto Organizador/organizador/{extensao}")
        pasta_ex.mkdir(exist_ok=True, parents=True) # criando pasta extensao

        shutil.move(arquivo, pasta_ex) # movendo

        # Data e hora atuais
        data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        with registro.open("a", encoding="utf-8") as f:
            f.write(f"Arquivo criado em: {data_atual}\n")
            f.write(f"{arquivo.stem}\n")
            f.write(f'Destino: {pasta_ex}\n\n')

        # Conts
        t_arquivo += 1
        if extensao not in ex:
            ex.append(extensao)

    print(f'Arquivos organizados: {t_arquivo}')
    print(f'Extensões encontradas: {ex}')
            
shutil.unpack_archive("Projeto Organizador/organizador.zip", "Projeto Organizador/organizador") # extraindo
organizador = Path("Projeto Organizador/organizador")
organizar(organizador)
