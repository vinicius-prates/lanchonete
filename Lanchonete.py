from time import *
import json

lanches = {1: "X-tudo", 2: "X-salada", 3: "Cheddar", 4: "X - Infurecido", 5: "Bacon especial"}
bebidas = {1: "Pink lemonade", 2: "Coca-cola", 3: "Guaraná", 4: "Suco natural de laranja", 5: "heineken"}
sobremesas = {1: "Banoffe", 2: "Churros", 3: "Corneto", 4: "Cheese Cake", 5: "Bolo Red Velvet"}
pedido = []


def main():

    print("Bem vindo a lanchonete do Prates!")
    sleep(2)

    while True:
        print("\n"*30)
        print("Qual cardápio você deseja ver?")
        print("1 - Lanches")
        print("2 - Bebidas")
        print("3 - Sobremesas")

        opcaocardapio = int(input("?>"))

        if opcaocardapio == 1:
            hamburgers()
        elif opcaocardapio == 2:
            drinks()
        else:
            deserts()

        print(pedido)
        continuar = input("Você deseja continuar com o pedido? (S/N)").lower()
        if continuar == 's':
            sleep(1)
        else:
            with open('pedido.txt', 'w') as f:
                f.write(json.dumps(pedido))

            print("Seu pedido final:")
            print(pedido)
            break


def hamburgers():
    print("\n" * 50)
    print("<HAMBURGUERS>")

    while True:

        sleep(1)
        print("1 - "+lanches.get(1))
        print("2 - "+lanches.get(2))
        print("3 - "+lanches.get(3))
        print("4 - "+lanches.get(4))
        print("5 - "+lanches.get(5))
        escolha = int(input("Digite o código do lanche desejado> "))

        lancheescolhido = lanches.get(escolha)
        pedido.append(lancheescolhido)
        print(pedido)

        revisar = input("Deseja adicionar mais algum lanche? (S/N)").lower()

        if revisar == 's':
            print()
        else:
            break


def drinks():
    print("\n" * 50)
    print("<DRINKS>")
    while True:

        sleep(1)
        print("1 - "+bebidas.get(1))
        print("2 - "+bebidas.get(2))
        print("3 - "+bebidas.get(3))
        print("4 - "+bebidas.get(4))
        print("5 - "+bebidas.get(5))
        escolha = int(input("Digite o código da bebida desejada> "))
        bebidaescolhida = bebidas.get(escolha)
        pedido.append(bebidaescolhida)
        print(pedido)

        revisar = input("Deseja adicionar mais alguma bebida? (S/N)").lower()

        if revisar == 's':
            print()
        else:
            break


def deserts():
    print("\n" * 50)
    print("<DESERTS>")
    while True:

        sleep(1)
        print("1 - " + sobremesas.get(1))
        print("2 - " + sobremesas.get(2))
        print("3 - " + sobremesas.get(3))
        print("4 - " + sobremesas.get(4))
        print("5 - " + sobremesas.get(5))
        escolha = int(input("Digite o código da sobremesa desejada> "))
        sobremesaescolhida = sobremesas.get(escolha)
        pedido.append(sobremesaescolhida)
        print("O seu pedido...")
        print(pedido)

        revisar = input("Deseja adicionar mais alguma sobremesa? (S/N)").lower()

        if revisar == 's':
            print()
        else:
            break


if __name__ == "__main__":
    main()
