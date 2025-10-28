from datetime import datetime

# Data completa
agora = datetime.now()
print(agora.day)
print(agora.month)
print(agora.year)

# Hora completa
print(agora.hour)
print(agora.minute)
print(agora.second)
print(agora.microsecond)

# Definição da Data manual
aniversario = datetime(2000, 5, 20)
print(aniversario.day)

## Criação a partir de variaveis 
ano = 2004
mes = 4
dia = 17
falso = datetime(ano, mes, dia) 
print(falso)

# Formatação da data
agora = datetime.now()
print(agora.strftime("Hoje é dia %d do mês %m do ano %Y"))
print(agora.strftime("Agora são %H horas e %M minutos"))

# Ler datas apartir de strings (transforma a str em objeto data)
data_str = "20/04/2025"
data_convertida = datetime.strptime(data_str, "%d/%m/%Y")
print(data_convertida)

# Exercicio
mes = agora.month

print(f"Hoje é o {mes}º mês do ano. Ainda faltam {12 - mes} meses para terminar o ano!")

def nome(nome):
    dia = agora.day
    mes = agora.strftime("%B") # nome completo do mês
    ano = agora.year
    hora = agora.hour
    minuto = agora.minute

    print(f"Assinatura gerada por {nome} em {dia} de {mes} de {ano} às {hora:02d}:{minuto:02d}")

nome("Raquel")