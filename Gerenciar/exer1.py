from pathlib import Path

# one
novo1 = Path("dados/entrada")
novo2 = Path("dados/saida")
novo3 = Path("relatorios")

novo1.mkdir(exist_ok=True, parents=True)
novo2.mkdir(exist_ok=True, parents=True)
novo3.mkdir(exist_ok=True)

# two
ar1 = Path("dados/entrada/dados1.txt")
ar2 = Path("dados/entrada/dados2.txt")
ar3 = Path("dados/entrada/dados3.txt")

ar1.touch()
ar2.touch()
ar3.touch()

# three
pasta = Path("dados/entrada")
for arquivo in pasta.glob("*.txt"):
    print(arquivo)