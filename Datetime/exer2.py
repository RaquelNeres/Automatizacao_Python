from datetime import datetime, timedelta

# one
novo = datetime(2025, 12, 31)
agora = datetime.now()
dif = novo - agora
print(dif.days)

# two
# evento_data = input("Digite a data do evento (ex: d/m/y): ")
# evento_data = datetime.strptime(evento_data, "%d/%m/%Y")

# evento = input("Digite uma data de um evento: ")
# doideira = evento.split()

# ano, mes, dia = map(int, doideira)
# evento = datetime(ano, mes, dia)

# if agora.day == evento.day and agora.month == evento.month:
#     print("está acontecendo hoje")
# elif agora < evento:
#     print(f'Faltam {(evento - agora).days}')
# else:
#     print("evento já aconteceu")

# Three
fabrica_cao = input("Digite a data do evento (ex: d/m/y): ")
fabrica_cao = datetime.strptime(fabrica_cao, "%d/%m/%Y")
mais = timedelta(days=180)
vencimento = fabrica_cao + mais

print(f'Validade: {vencimento}')
if vencimento > agora:
    print("Valido")
    print(f'Faltam {(vencimento - agora).days}')
else:
    print("Venceu")
    print(f'Ja passou {(vencimento - agora).days}')