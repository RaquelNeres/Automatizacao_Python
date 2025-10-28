from pathlib import Path

# Caminhos Simples
caminho = Path("arquivinho.txt")
caminho_absoluto = caminho.absolute()  

print(caminho_absoluto) # mostra o caminho completo  (des do inicio do pc)

print(caminho) # mostra o caminho apartir da pasta atual do codigo

# Verificação
caminho = Path("arquivinho.txt")
if caminho.exists():
    print("Existe!")
else:
    print("Existe não!")

# Verificação de tipo 
caminho = Path("pastinha")

if caminho.is_file():  # arquivo 
    print("É arquivo!")
elif caminho.is_dir(): # pasta
    print("É uma pasta!")

# Criação
nova_pasta = Path("NovaPasta/outraPasta/maisUmaPasta")
nova_pasta.mkdir(exist_ok=True, parents=True) # criar sem reclamar

# Excluir
arquivinho = Path("arquivinho.txt")
novapasta = Path("NovaPasta")

arquivinho.unlink() # remover arquivos
novapasta.rmdir() # removar pastas

# Ler
arquivinho = Path("arquivinho.txt")
texto = arquivinho.read_text() # ler
print(texto)
arquivinho.write_text("Alguma frase aí", encoding='utf-8') # escrever

# Procurar
pasta = Path("minha_pasta")
# .iterdir() busca na pasta toda
for arquivo in pasta.glob("*.txt"): # filtar por .txt
    print(arquivo)

# Algo especifico do caminho
caminho = Path("minha_pasta/dados.xlsx")

print(caminho) # Caminho

print(caminho.name) # nome e extensao

print(caminho.stem) # nome sem extensão

print(caminho.suffix) # extesão

arquivo = Path("uuu/meu_arquivo.txt")
arquivo.touch() # criar arquivo