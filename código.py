import os

shopping_list = []

while True:

    print('Lista Mercado:')
    for indice, item in enumerate(shopping_list, start = 1):
                print(f'{indice} - {item}')
    if not shopping_list:
         print('Não há nada na lista')
    print('Selecione uma opção')
    opcao = input('[i]nserir, [a]pagar, [l]istar ou [s]air: ')

    if opcao == 'i':
        item = input('Digite um item que deseja inserir na lista: ')
        shopping_list.append(item)
        os.system('cls')
        print('Item inserido')

    elif opcao == 'a':
        for indice, item in enumerate(shopping_list, start = 1):
                print(f'{indice} - {item}')
        try:
            indice = int(input('Digite o índice que deseja apagar: ')) - 1
            del shopping_list[indice]
            os.system('cls')
            print('Item apagado')
        except ValueError:
            print('Digite o número do item')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')

    elif opcao == 'l':
        if not shopping_list:
            print('Não há nada na lista')
        else:
            for indice, item in enumerate(shopping_list, start = 1):
                print(f'{indice} - {item}')

    elif opcao == 's':
        print('Encerrando o programa...')
        os.system('cls')
        break

    else:
        print('Escolha somente [i], [a], [l] ou [s]')

    input('Pressione Enter para continuar...')
    os.system('cls')
