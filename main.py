import json

def read_json(path):
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = json.load(f)
            return content
    except FileNotFoundError:
        return "Arquivo não encontrado"
    except json.JSONDecodeError:
        return "Json Inválido"

if __name__ == '__main__':
    cont = read_json('carteira.json')
    print (cont)