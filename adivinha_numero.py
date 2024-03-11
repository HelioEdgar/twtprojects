import random


limite = input("Digite um número: ")

if limite.isdigit():
    limite = int(limite)

    if limite <= 0:
        print("Digite um número maior que zero na próxima vez!")
        quit()
    
else:
    print("Digite um número da próxima vez!")
    quit()

n = random.randint(0, limite)
tentativa = 0

print("Bem-vindo ao jogo de adivinha! Tente adivinhar o número que estou a pensar. Dica: é um número entre 0 e",limite)

while True:
    tentativa += 1
    res = input("Adivinhe o número: ")

    if res.isdigit():
        res = int(res)

    else:
        print("Digite um número da próxima vez!")
        continue

    if res == n:
        print("Acertou!!!")
        break
    elif res > n:
        print("É um número menor!")
    else:
        print("É um número maior!")
        

print(f"Você tentou {tentativa} vezes")