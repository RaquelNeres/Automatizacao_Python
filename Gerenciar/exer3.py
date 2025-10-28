from pathlib import Path
from datetime import datetime

# # Caminho do arquivo
# arquivo = Path("relatorio.txt")

# # Texto base
# texto = "Estou aprendendo Python!"

# # Data e hora atuais
# data_atual = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

# # Escreve o texto e depois a data
# with arquivo.open("w", encoding="utf-8") as f:
#     f.write(texto + "\n")
#     f.write(f"Arquivo criado em: {data_atual}\n")

# print("Relatório criado com sucesso!")



# # 2
# a = Path("mensagem.txt")
# a.touch()

# with open("mensagem.txt", 'r+', encoding='utf-8') as mensagem:
#     mensagem.write("Ariba baby!\n")

#     # Lê o conteúdo do arquivo
#     conteudo = mensagem.read()

#     # Conta apenas as letras (ignorando espaços e pontuação)
#     contador = 0
#     for c in conteudo:
#         if c.isalpha():
#             contador += 1

#     print(f"O arquivo contém {contador} letras.")



# 3
arquivo_log = Path("acesso.log")

with open(arquivo_log, "r+", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()  # cria uma lista, cada item é uma linha

# remover espaçõs e colocar em maiusculo
chave = input("Digite a palavra-chave (ex: ERROR, INFO, WARNING): ").strip().upper()

encontradas = []

for linha in linhas:
    if chave in linha.upper():
        encontradas.append(linha.strip())  # strip remove espaços e quebras de linha extras

if len(encontradas) > 0:
    print(f"\nLinhas contendo '{chave}':\n")
    for linha in encontradas:
        print(linha)
else:
    print(f"\nNenhuma linha contendo '{chave}' foi encontrada.")
