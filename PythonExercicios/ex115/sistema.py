from lib import interface
from lib import arquivo
while True:
    interface.titulo('MENU PRINCIPAL')
    interface.pintar(33, '1', '-', 34, 'Ver pessoas cadastradas')
    interface.pintar(33, '2', '-', 34, 'Cadastrar mais uma pessoa')
    interface.pintar(33, '3', '-', 34, 'Sair do programa')
    opc = interface.repetir('\033[31mERRO! Por favor digite uma opção valida!\033[m', '123')
    if opc == '3':
        interface.sair('Saindo do sistema... Até logo!')
        break
    if opc == '2':
        interface.titulo('NOVO ARQUIVO')
        nome = str(input('Nome: '))
        idade = str(input('Idade: '))
