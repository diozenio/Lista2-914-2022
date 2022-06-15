jogos = ["Valorant", "CSGO", "Fortnite"]
salgados = ["Coxinha", "Batata Frita", "Canudinho"]
ingredientes = ["Queijo", "Molho de tomate", "Presunto"]

listona = []
listona.append(jogos)
listona.append(salgados)
listona.append(ingredientes)

print("------ Listona ------")
for x in listona:
    print(x)

print("------- B -------")
print(listona[1][0])

print("------- C -------")
listona[1].append("Coxinhas")
listona[1].append("Coxinhas")
listona[1].append("Coxinhas")
listona[1].append("Coxinhas")
for x in listona:
    print(x)
print("\nAgora a listona de salgados tem VÁRIAS coxinhas!!!")

print("------- D -------")
listona[2].append("Coca-cola")
listona[2].append("Suco")
listona[2].append("Água")
for x in listona:
    print(x)

