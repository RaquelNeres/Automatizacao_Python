from openpyxl import load_workbook
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from datetime import datetime

arquivo = load_workbook('Projeto Academico/alunos.xlsx')
alunos = arquivo['Alunos']

arquivo = Workbook()
reprovados = arquivo.active
reprovados.title = "Reprovados"

arquivo = Workbook()
aprovados = arquivo.active
aprovados.title = "Aprovados"

apro = 0
repro = 0
total = 0
cont = 0
maior = 1
nome = "a"

for linha in alunos.iter_rows(values_only=True, min_row=2, max_row=20):
    Nome, Curso, Idade, Nota, Matrícula = linha
    total += Nota
    cont += 1
    if Nota > maior:
        maior = Nota
        nome = Nome

    if Nota >= 7:
        aprovados.append(['Nome, Curso, Idade, Nota Final, Data de Matrícula'])
        aprovados.append(Nome, Curso, Idade, Nota, Matrícula)
        apro+=1
    else:
        reprovados.append(['Nome, Curso, Idade, Nota Final, Data de Matrícula'])
        reprovados.append(Nome, Curso, Idade, Nota, Matrícula)
        repro+=1


print(f"Aprovados: {apro}")
print(f"Reprovados: {repro}")
print(f"Média da turma {total/cont}")
print(f"Aluno com a maior nota: {nome}")

reprovados.save('Projeto Academico/planilhas_criadas/reprovados.xlsx')
aprovados.save('Projeto Academico/planilhas_criadas/aprovados.xlsx')