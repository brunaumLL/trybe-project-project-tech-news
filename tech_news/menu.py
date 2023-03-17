import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.ratings import top_5_news, top_5_categories
from tech_news.analyzer.search_engine import (
    search_by_title, search_by_date,
    search_by_tag,
    search_by_category
    )


def case0():
    res = input("Digite quantas notícias serão buscadas:")
    return get_tech_news(res)


def case1():
    res = input("Digite o título:")
    return search_by_title(res)


def case2():
    res = input("Digite a data no formato aaaa-mm-dd:")
    return search_by_date(res)


def case3():
    res = input("Digite a tag:")
    return search_by_tag(res)


def case4():
    res = input("Digite a categoria:")
    return search_by_category(res)


def case5():
    return top_5_news()


def case6():
    return top_5_categories()


def case7():
    sys.stdout.write("Encerrando script\n")


def caseInvalid():
    print("Opção inválida", file=sys.stderr)


switch = {
    "0": case0,
    "1": case1,
    "2": case2,
    "3": case3,
    "4": case4,
    "5": case5,
    "6": case6,
    "7": case7,
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
