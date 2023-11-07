import pyautogui
from time import sleep


# função de continuação OperaXG
def operaXG():
    finalizacao = pyautogui.confirm("Deseja finalizar o processo por aqui? ")

    if finalizacao == 'OK':
        pyautogui.alert("Ok, muito obrigado por testar a versão prototipo da Annie.")

    else:
        pyautogui.alert("Ok, vamos continuar a brincadeira...")


# função de continuação Xbox
def xbox():
    finalizacao = pyautogui.confirm("Deseja finalizar o processo por aqui? ")

    if finalizacao == 'OK':
        pyautogui.alert("Ok, muito obrigado por testar a versão prototipo da Annie.")

    else:
        pyautogui.alert("Ok, vamos continuar a brincadeira...")


# começa o main do codigo
pyautogui.alert('''Olá, seja bem vindo ao prototipo de assistente virtual.
                               Me chamo Annie.''')

pyautogui.alert('''Estou aqui para lhe ajudar em suas tarefas do dia a dia. 
Atualmente estou com apenas 3 funcionalidades''')

entrada_de_dados = pyautogui.prompt('''1-Pycharm   2-Xbox   3-Opera XG''')

# Aqui era para ele rodar o While caso o usuario digitasse uma opção errada.
while True:
    try:
        entrada_de_dados = int(entrada_de_dados)

        if entrada_de_dados == 1:
            sleep(1)
            pyautogui.moveTo(x=1460, y=1051)
            pyautogui.click()
            break

        elif entrada_de_dados == 2:
            sleep(1)
            pyautogui.moveTo(x=1347, y=1048)
            pyautogui.click()
            sleep(4)
            xbox()
            break

        elif entrada_de_dados == 3:
            sleep(1)
            pyautogui.moveTo(x=1075, y=1055)
            pyautogui.click()
            sleep(4)
            operaXG()
            break

        else:
            print("Opção inválida, faça novamente")
            continue

    except ValueError:
        print("Entrada inválida, digite um número válido.")
        break
