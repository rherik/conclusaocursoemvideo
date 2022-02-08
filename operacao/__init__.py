from menu.interface import *
def arquivoExiste(nome):
    try:
        arq = open(nome, 'rt')
        arq.close()
    except(FileNotFoundError):
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        arq = open(nome, 'wt+')
        arq.close()
    except:
        print('Houve um erro na criação do arquivo.')
    else:
        print(f'O arquivo {nome} foi criado com sucesso.')


def lerArquivo(nome):
    try:
        arq = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo.')
    else:
        cabecalho('Pessoas cadastradas')
        for linha in arq:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'Nome: {dado[0]:<10} Idade: {dado[1]:>3}')
    finally:
        arq.close()


def cadastrar(a, nome='Desconhecido', idade=0):
    try:
        arq = open(a, 'at')
    except:
        print('Houve um erro na abertura do arquivo.')
    else:
        try:
            arq.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro ao escrever os dados.')
        else:
            print(f'Novo registro de {nome} adicionado.')
            arq.close()
