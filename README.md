# Gestor de Portfólio de Cripto (CLI)

Um projeto em Python modular e assente na linha de comandos (CLI) que lê um ficheiro de carteira local em JSON, consulta os preços atualizados em tempo real através da API REST da CoinGecko e exibe o resumo financeiro totalmente formatado no terminal.

---

## Funcionalidades

- **Consulta em Tempo Real:** Integração com a API pública da CoinGecko para cotações em USD.
- **Leitura Defensiva de JSON:** Suporta múltiplos formatos de ficheiro de carteira e trata falhas de leitura ou sintaxe de forma segura.
- **Interface CLI Organizada:** Exibição em formato de tabela com alinhamento de colunas, separadores de milhar e precisão decimal.
- **Arquitetura Modular:** Separação clara de responsabilidades por módulos/ficheiros (`read_json`, `get_price`, `show_res`).
- **Código Limpo (Clean Code):** Tipagem estática com *Type Hints* (módulo `typing`) e zero *warnings* em analisadores como o PyCharm.

---

## Tecnologias Utilizadas

- **Linguagem:** [Python 3.10+](https://www.python.org/)
- **Biblioteca HTTP:** [Requests](https://requests.readthedocs.io/)
- **API REST:** [CoinGecko API v3](https://www.coingecko.com/en/api)

---

## Estrutura do Projeto

```text
├── main.py              # Ponto de entrada da aplicação
├── read_json.py         # Módulo para leitura e validação do ficheiro JSON
├── get_price.py         # Módulo para integração com a API da CoinGecko
├── show_res.py         # Módulo responsável pela formatação da saída no terminal
├── carteira.json        # Ficheiro de dados com as criptomoedas e quantidades
└── README.md            # Documentação do projeto
