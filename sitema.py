from menu.operacao import *
from time import sleep
arquivo = 'menu.txt'
if arquivoExiste(arquivo):
    print('Arquivo encontrado.')
else:
    print('Arquivo não encontrado.')
    criarArquivo(arquivo)

while True:
    resposta = menu(['Ver cadastrados', 'Cadastrar pessoas', 'Sair do sistema'])
    if resposta == 1:
        # Opção de listar o conteúdo de um arquivo
        lerArquivo(arquivo)
    elif resposta == 2:
        # Opção de cadastrar uma nova pessoa
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arquivo, nome, idade)
    elif resposta == 3:
        # Opção para sair do sistema
        cabecalho('Saindo do sistema... Até logo.')
        break
    else:
        # Digitou uma opção errada no menu
        print('\033[31mDigite uma opção válida.\033[m')
    sleep(0.5)
