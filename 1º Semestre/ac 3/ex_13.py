team1 = input("Digite o primeiro time: ")
gols1 = int(input("Digite o número de gols: ")) 
team2 = input("Digite o segundo time: ")
gols2 = int(input("Digite o número de gols: "))

if gols1 > gols2:
    print(f"O {team1} venceu a partida.")

elif gols1 < gols2:
    print(f"O {team2} venceu a partida.")

else:
    print(f"O {team1} e {team2} ficaram no empate.")
