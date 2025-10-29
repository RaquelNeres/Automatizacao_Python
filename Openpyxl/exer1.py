from openpyxl import Workbook

# 1
arquivo = Workbook()
planilha = arquivo.active
planilha.title = "Pessoas"

planilha["A1"] = "Nome"
planilha["A2"] = "João"
planilha["A3"] = "Marina"
planilha["A4"] = "Otávio"

planilha["B1"] = "Cidade"
planilha["B2"] = "Recife"
planilha["B3"] = "São Paulo"
planilha["B4"] = "Belo Horizonte"

# 2
planilha.append(['Letícia', 'Porto Alegre'])
planilha.append(['Gustavo', 'Salvador'])

# 3
arquivo.create_sheet("Visitas")
visitas = arquivo['Visitas']
visitas.append(['Data', 'Visitantes'])
visitas.append(['01/01/2025', '134'])
visitas.append(['02/01/2025', '156'])

visitas['B2'] = 142

arquivo.save("Openpyxl/planilhas_criadas/cadastro.xlsx")