import os

def calculadora():
    op = input('''
Escolha a operação a ser executada:
    + para adição
    - para subtração
    * para mutiplicação
    / para divisão
''')


    if op == '+':
        num_1 = int(input('Informe o primeiro número: '))
        num_2 = int(input('Informe o segundo número: '))
        print('{} + {} = '.format(num_1, num_2),'', num_1 + num_2)

    elif op == '-':
        num_1 = int(input('Informe o primeiro número: '))
        num_2 = int(input('Informe o segundo número: '))
        print('{} - {} = '.format(num_1, num_2),'', num_1 - num_2) 

    elif op == '*':
        num_1 = int(input('Informe o primeiro número: '))
        num_2 = int(input('Informe o segundo número: '))
        print('{} * {} = '.format(num_1, num_2),'', num_1 * num_2)

    elif op == '/':
        num_1 = int(input('Informe o primeiro número: '))
        num_2 = int(input('Informe o segundo número: '))
        if num_1 ==0:
            print('Não é possível realizar uma divisão pro 0')
        else:
            print('{} / {} = '.format(num_1, num_2),'', num_1 / num_2)

    else:
        print('Operação inválida !')

    repetir()

def repetir():
    op_repetir = input('''
Quer realizar uma nova operação?
S para SIM ou N para NÃO.
''')

    if op_repetir.upper() == 'S':
        os.system('cls') or None
        calculadora()
    elif op_repetir.upper() == 'N':
        print('Obrigado por utilizar o sistema.')
    else:
        repetir()

calculadora()