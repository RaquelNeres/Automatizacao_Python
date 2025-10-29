import random

convidados = ["Ana", "Lucas", "João", "Marina", "Pedro", "Carla", "Ricardo", "Fernanda"]
premios = ["Bicicleta", "Tablet", "Fone de ouvido", "Livro", "Camisa"]

convidados_embaralhados = random.sample(convidados, len(premios))
premios_embaralhados = random.sample(premios, len(premios))

for i, _ in enumerate(premios):
    print(f'O premio de {convidados_embaralhados[i]} é {premios_embaralhados[i]}')