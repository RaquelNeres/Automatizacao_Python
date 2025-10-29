import random 

inteiro_aleatorio = random.randint(1, 60)
float_aleatorio = random.uniform(1, 20)

cartas = ['Ás', 'Rei', 'Rainha', 'Valete']
carta_aleatoria = random.choice(cartas) # 1 aleatoria de lista
carta_aleatoria = random.choices(cartas, k=2) # varias aleatorias de lista
carta_aleatoria = random.sample(cartas, k=2) # nao repetir a escolha aleatoria

print(f"As cartas escolhidas foi: {carta_aleatoria}")

musicas = ['musica1', 'musica2', 'musica3', 'musica4']
random.shuffle(musicas) # muda a ordem da lista