from read_json import read_json
from get_price import get_price
from show_res import show_port

if __name__ == '__main__':
    cont = read_json('carteira_01.json')
    if cont is not None:
        coin = get_price(cont)
        if coin is not None:
            show_port(cont, coin)
    else:
        print ("Não foi possível carregar a carteira")
