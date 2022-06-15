doador = {
    "idade": int(input("Digite sua idade: \n")),
    "peso": int(input("Digite seu peso: \n")),
    "horas": int(input("Digite a quantidade de horas que você dormiu nas últimas 24h: \n")),
}

if doador["idade"] >= 16 and doador["idade"] <= 69 and doador["peso"] >= 50 and doador["horas"] >= 6:
    print("Pode doar!")
else:
    print("Não pode doar!")
