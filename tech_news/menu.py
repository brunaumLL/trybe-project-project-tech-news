import sys


def case0():
    return input("Digite quantas notícias serão buscadas:")


def case1():
    return input("Digite o título:")


def case2():
    return input("Digite a data no formato aaaa-mm-dd:")


def case3():
    return input("Digite a tag:")


def case4():
    return input("Digite a categoria:")


def caseInvalid():
    print("Opção inválida", file=sys.stderr)


switch = {
    "0": case0,
    "1": case1,
    "2": case2,
    "3": case3,
    "4": case4,
}


# Requisito 12
def analyzer_menu():
    select = input(
        "Selecione uma das opções a seguir:\n"
        " 0 - Popular o banco com notícias;\n"
        " 1 - Buscar notícias por título;\n"
        " 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n"
        " 4 - Buscar notícias por categoria;\n"
        " 5 - Listar top 5 notícias;\n"
        " 6 - Listar top 5 categorias;\n"
        " 7 - Sair.\n")

    if select in switch:
        return switch[select]()
    else:
        return caseInvalid()
