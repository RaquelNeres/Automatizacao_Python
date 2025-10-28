arquivo = open("arquivo.txt")
conteudo = arquivo.read()

print(conteudo)
arquivo.close()

with open("arquivo.txt") as arquivo:
    print(arquivo.readlines()) # ler as linhas do arquivo


with open("arquivo.txt", 'a', encoding='utf-8') as arquivo:
    arquivo.write("Olá mundo!\n") # escreve formato pt sem apagar oque ta no arquivo

with open("arquivo.txt", 'r+', encoding='utf-8') as arquivo: # ler e escrever sem apagar o conteudo 
    arquivo.write("Olá, mundo!")
    # arquivo.seek(0)
    arquivo.write("Texto que vem depois")
    print(arquivo.read())