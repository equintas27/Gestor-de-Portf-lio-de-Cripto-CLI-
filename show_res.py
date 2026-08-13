from typing import Dict, Any, Optional

def show_port(carteira:Dict[str, Any], price: Dict[str, Any])-> Optional[Dict[str, Any]]:
    total_carteira = 0.0
    print ("\n" + "=" * 50)
    print (f"{'RESUMO DA CARTEIRA':^50}")
    print("=" * 50)
    print(f"{'Moeda':<9} {'Qtd.':>10} {'Preço Unit.':>14} {'Total (USD)':>12}")
    print("=" * 50)
    for moeda, dados in carteira.items():
        if isinstance(dados, dict):
            qtd = dados.get('quantidade', 0.0)
        else:
            qtd = dados
        prec_unit = float(price.get(moeda, {}).get('usd', 0.0))
        try:
            qtd_num = float(qtd)
        except (ValueError, TypeError):
            qtd_num = 0.0
        subtotal = qtd_num * prec_unit
        total_carteira += subtotal
        print (f"{moeda.capitalize():<9} {qtd_num:>10.4f} {f'$ {prec_unit:,.2f}':>14} {f'$ {subtotal:,.2f}':>12}")
    print("-" * 50)
    print(f"{'TOTAL CARTEIRA:':>30} {f'${total_carteira:,.2f}':>12}")
    print("=" * 50)
