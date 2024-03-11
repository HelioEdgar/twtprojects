print("Bem-vindo ao Jogo de Questões sobre League of Legends!")

correcto = []
errado = []

play = input("Queres jogar? ").lower()

if play != "sim":
    quit()

print("OK! Bora lá")

res = input("O que significa LoL? ").lower()

if res == "league of legends":
    correcto.append(res)
else:
    errado.append(res)

res = input("O que significa KDA? ").lower()

if res == "kill death assist":
    correcto.append(res)
else:
    errado.append(res)

res = input("O que significa MIA? ").lower()

if res == "missing in action":
    correcto.append(res)
else:
    errado.append(res)

print("Acertaste", len(correcto), "questões!") 
print("As respostas:", correcto)
print("Erraste", len(errado), "questões!") 
print("As respostas:", errado)