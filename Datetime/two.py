from datetime import datetime, timedelta

hoje = datetime.now()
um_dia = timedelta(days=1)

# Operações matematicas com a data
amanha = hoje + um_dia
ontem = hoje - um_dia
print(ontem) 

# Comparação de datas 
prazo = datetime(2025, 7, 20)
hoje = datetime.now()

## Excel: SE
if hoje > prazo:
    print("Prazo vencido!")
else:
    print("Ainda está no prazo.")

# Operação de comparação de datas
agora = datetime.now()
futuro = datetime(2025, 9, 23)
dias_restantes = futuro - agora
print(dias_restantes.days)

# Projeto completo de comparação
aniversario = datetime(2025, 7, 22)
hoje = datetime.now()

if aniversario.day == hoje.day and aniversario.month == hoje.month:
    print("Hoje é o dia do aniversário!")
elif aniversario > hoje:
    print("O aniversário ainda vai acontecer!")
elif aniversario < hoje:
    print("Já passou o aniversário!")